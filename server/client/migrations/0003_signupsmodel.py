# Generated by Django 4.2.9 on 2024-01-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_celebritiesmodel_category_celebritiesmodel_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
