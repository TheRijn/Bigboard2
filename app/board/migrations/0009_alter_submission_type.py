# Generated by Django 3.2.7 on 2021-10-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20211013_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='type',
            field=models.CharField(choices=[('T', 'Trie'), ('H', 'Hashtable')], default='H', max_length=1, verbose_name='Data structure'),
        ),
    ]
