# Generated by Django 3.2.4 on 2021-06-14 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_nome_product_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='variation',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
    ]
