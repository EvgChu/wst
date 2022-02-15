# Generated by Django 3.2.7 on 2022-02-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='aauthor',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
