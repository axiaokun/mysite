# Generated by Django 2.2 on 2020-08-11 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200811_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readnum',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog'),
        ),
    ]
