# Generated by Django 4.0.3 on 2022-03-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapi', '0002_alter_product_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]