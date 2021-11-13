# Generated by Django 3.2.9 on 2021-11-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211112_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinks',
            name='english_name',
        ),
        migrations.RemoveField(
            model_name='drinks',
            name='korean_name',
        ),
        migrations.AddField(
            model_name='drinks',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='drinks',
            name='name',
            field=models.CharField(max_length=45, null=True),
        ),
    ]