# Generated by Django 4.2.9 on 2024-01-16 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebritiesmodel',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='client.categorymodel'),
        ),
        migrations.AddField(
            model_name='celebritiesmodel',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
