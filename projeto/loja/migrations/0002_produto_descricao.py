# Generated by Django 4.0.1 on 2022-01-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.TextField(default='', max_length=1000),
        ),
    ]