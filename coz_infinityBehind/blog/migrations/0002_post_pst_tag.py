# Generated by Django 2.0.5 on 2018-10-14 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pst_tag',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
