# Generated by Django 4.2 on 2024-05-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0002_artwork_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='daily_views',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
