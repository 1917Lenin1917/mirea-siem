# Generated by Django 5.0.6 on 2024-05-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='category',
            field=models.CharField(choices=[('normal', 'Обычные'), ('network', 'Сетевые')], default='normal', max_length=100),
        ),
    ]
