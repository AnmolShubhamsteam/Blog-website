# Generated by Django 5.0.4 on 2024-06-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=122),
        ),
    ]
