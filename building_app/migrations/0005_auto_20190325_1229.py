# Generated by Django 2.1.5 on 2019-03-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_app', '0004_apartment_extras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='extras',
            field=models.CharField(choices=[('JCZ', 'jacuzzi'), ('SAU', 'suana'), ('STU', 'studio')], default='studio', max_length=3),
        ),
    ]
