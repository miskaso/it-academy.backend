# Generated by Django 5.0.7 on 2024-07-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leed',
            old_name='password',
            new_name='contacts',
        ),
        migrations.RemoveField(
            model_name='leed',
            name='email',
        ),
        migrations.AddField(
            model_name='leed',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]