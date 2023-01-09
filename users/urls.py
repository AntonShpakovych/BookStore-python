from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views
from users.forms import CustomUserPasswordResetForm


urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.log_out, name='logout'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/pages/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(form_class = CustomUserPasswordResetForm, template_name='users/pages/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='users/pages/password_reset_complete.html'), name='password_reset_complete'),
    path('settings/address/', views.setting_address, name='address'),
    path('settings/privacy/', views.setting_privacy, name='privacy'),
    # path('settings/change_email/', views.change_email, name='change_email'),
    path('settings/delete_account/<int:id>/', views.delete_account, name='delete_account'),
    # path('settings/change_password/', views.change_password, name='change_password')
]
