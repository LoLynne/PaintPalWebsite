# Generated by Django 4.1.5 on 2023-07-29 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0005_profile_paintusedgallons_profile_paintusedliters'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prevPaintUsedGallons',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='prevPaintUsedLiters',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
