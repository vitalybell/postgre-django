# Generated by Django 5.1.2 on 2024-10-22 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_buyer_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='buyer',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
