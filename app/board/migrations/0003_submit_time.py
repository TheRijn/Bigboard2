# Generated by Django 3.2.7 on 2021-10-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_submit'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='time',
            field=models.DecimalField(decimal_places=4, max_digits=7, null=True),
        ),
    ]
