# Generated by Django 4.2.2 on 2023-06-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_endereco_cliente_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(choices=[('MG', 'Minas Gerais'), ('SP', 'Sao Paulo'), ('RJ', 'Rio de Janeiro')], max_length=2),
        ),
    ]
