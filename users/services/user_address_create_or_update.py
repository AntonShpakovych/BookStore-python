from users.models import BillingAddress, ShippingAddress
from users.forms import BillingAddressForm, ShippingAddressForm

class UserAddressCreateOrUpdate:
    BILLING_ADDRESS = BillingAddress.__name__
    ShippingAddress = ShippingAddress.__name__

    def __init__(self, user, type, request_data):
        self.user = user
        self.type = type
        self.request_data = request_data

    def call(self):
        self._generate_dormant_form()

        if self._is_need_update():
            self._active_form_when_update()
            self._updating()
        else:
            self._active_form_when_create()
            self._creating()

        
    def _creating(self):
        if self.active_form.is_valid():
            address = self.active_form.save()

            if self.is_billing():
                self.user.billing_address = address
            else:
                self.user.shipping_address = address
            self.user.save()
                
    def _updating(self):
        if self.active_form.is_valid():
            self.active_form.save()

    def _generate_dormant_form(self):
        if self.is_billing():
            self.dormant_form = ShippingAddressForm(instance=self.user.shipping_address)
        else:
            self.dormant_form = BillingAddressForm(instance=self.user.billing_address)


    def _active_form_when_create(self):
        self.active_form = self._billing_form_create() if self.is_billing() else self._shipping_form_create()

    def _active_form_when_update(self):
        self.active_form = self._billing_form_update() if self.is_billing() else self._shipping_form_update()

    def is_billing(self):
        return self.type == self.BILLING_ADDRESS

    def _is_need_update(self):
        return self.user.billing_address if self.is_billing() else self.user.shipping_address

    def _billing_form_update(self):
        return BillingAddressForm(self.request_data, instance=self.user.billing_address)

    def _shipping_form_update(self):
        return ShippingAddressForm(self.request_data, instance=self.user.shipping_address)
    
    def _billing_form_create(self):
        return BillingAddressForm(self.request_data)

    def _shipping_form_create(self):
        return ShippingAddressForm(self.request_data)
