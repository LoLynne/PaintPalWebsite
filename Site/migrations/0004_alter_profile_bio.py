# Generated by Django 4.1.5 on 2023-06-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='none', max_length=500),
            preserve_default=False,
        ),
    ]
