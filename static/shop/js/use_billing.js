function useBilling(element){
    let billing_inputs = document.getElementById('billing-address').getElementsByClassName('form-control')
    let shipping_inputs = document.getElementById('shipping-address').getElementsByClassName('form-control')
   
    for (let input in shipping_inputs){
        shipping_inputs[input].value = billing_inputs[input].value
    }
}
