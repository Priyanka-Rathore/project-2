# Generated by Django 2.2.5 on 2021-02-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_tech_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech_support',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]