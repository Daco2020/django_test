# Generated by Django 3.2.9 on 2021-11-12 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allergy_drink',
            old_name='allergy_id',
            new_name='allergy',
        ),
        migrations.RenameField(
            model_name='allergy_drink',
            old_name='drink_id',
            new_name='drink',
        ),
        migrations.RenameField(
            model_name='categories',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='drinks',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='drink_id',
            new_name='drink',
        ),
    ]
