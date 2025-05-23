# Generated by Django 4.2 on 2024-10-26 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0006_product_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='partner.partner')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='catalogue.product')),
            ],
        ),
    ]
