# Generated by Django 3.1.2 on 2022-10-01 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0002_alter_login_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]