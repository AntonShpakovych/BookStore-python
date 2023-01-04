# Generated by Django 4.1.2 on 2023-01-04 15:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import users.validation


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[users.validation.ValidationUserAddress.first_name_validation, django.core.validators.MinLengthValidator(3)])),
                ('last_name', models.CharField(max_length=50, validators=[users.validation.ValidationUserAddress.last_name_validation, django.core.validators.MinLengthValidator(3)])),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50, validators=[users.validation.ValidationUserAddress.city_validation, django.core.validators.MinLengthValidator(3)])),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=10, validators=[users.validation.ValidationUserAddress.zip_validation, django.core.validators.MinLengthValidator(5)])),
                ('address', models.CharField(max_length=50, validators=[users.validation.ValidationUserAddress.address_validation, django.core.validators.MinLengthValidator(3)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[users.validation.ValidationUserAddress.first_name_validation, django.core.validators.MinLengthValidator(3)])),
                ('last_name', models.CharField(max_length=50, validators=[users.validation.ValidationUserAddress.last_name_validation, django.core.validators.MinLengthValidator(3)])),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50, validators=[users.validation.ValidationUserAddress.city_validation, django.core.validators.MinLengthValidator(3)])),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip', models.CharField(max_length=10, validators=[users.validation.ValidationUserAddress.zip_validation, django.core.validators.MinLengthValidator(5)])),
                ('address', models.CharField(max_length=50, validators=[users.validation.ValidationUserAddress.address_validation, django.core.validators.MinLengthValidator(3)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='billing_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='users.billingaddress'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='shipping_address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='users.shippingaddress'),
        ),
    ]
