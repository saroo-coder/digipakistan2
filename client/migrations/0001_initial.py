# Generated by Django 3.1.6 on 2021-05-18 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password_at_time_of_creation', models.CharField(max_length=13)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_users.user')),
            ],
        ),
    ]
