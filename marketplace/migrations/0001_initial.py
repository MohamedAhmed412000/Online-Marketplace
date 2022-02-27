# Generated by Django 4.0.2 on 2022-02-25 08:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=80, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hideEmail', models.BooleanField(default=True)),
                ('balance', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(default='', max_length=200)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('recommend', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.CharField(choices=[('Digital Devices', 'Digital Devices'), ('Clothes', 'Clothes'), ('Sport', 'Sport'), ('Food', 'Food'), ('Home Devices', 'Home Devices'), ('Other', 'Other')], default=1, max_length=15)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productOwner', to='marketplace.account')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('date_buy', models.DateTimeField(auto_now_add=True, verbose_name='date buy')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='marketplace.account')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productsBought', to='marketplace.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='marketplace.account')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productsMarket', to='marketplace.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marketOwner', to='marketplace.account')),
            ],
            options={
                'unique_together': {('user', 'product')},
                'index_together': {('user', 'product')},
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='marketplace.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartOwner', to='marketplace.account')),
            ],
            options={
                'unique_together': {('user', 'product')},
                'index_together': {('user', 'product')},
            },
        ),
    ]