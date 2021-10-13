# Generated by Django 3.2.7 on 2021-10-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_rename_submit_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='ip',
            field=models.GenericIPAddressField(protocol='IPv4', verbose_name='IP-address'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='staff',
            field=models.BooleanField(default=False, verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='state',
            field=models.CharField(choices=[('SU', 'Submitted'), ('RU', 'Running'), ('AC', 'Accepted'), ('RE', 'Rejected'), ('DE', 'Deleted')], default='SU', max_length=2),
        ),
        migrations.AlterField(
            model_name='submission',
            name='student_number',
            field=models.PositiveIntegerField(verbose_name='Student number'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission',
            field=models.FileField(upload_to='static/uploads', verbose_name='Submission'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='type',
            field=models.CharField(choices=[('T', 'Trie'), ('H', 'Hashtable')], max_length=1, verbose_name='Data structure'),
        ),
    ]
