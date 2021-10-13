# Generated by Django 3.2.7 on 2021-10-13 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20211013_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dictionary',
            options={'verbose_name': 'Dictionary', 'verbose_name_plural': 'Dictionaries'},
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.dictionary')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.text')),
            ],
            options={
                'unique_together': {('text', 'dictionary')},
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('testcases', models.ManyToManyField(related_name='used_in', to='board.TestCase')),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submissions', to='board.board'),
        ),
    ]