# Generated by Django 4.1.1 on 2022-10-15 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0006_registration_address_alter_login_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Feedbacks', models.CharField(max_length=100)),
                ('fid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='farmapp.registration')),
            ],
        ),
    ]