# Generated by Django 4.0.4 on 2022-04-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0004_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='clave',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
