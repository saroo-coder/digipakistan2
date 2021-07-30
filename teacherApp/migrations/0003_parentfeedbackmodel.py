# Generated by Django 3.2 on 2021-07-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_auto_20210712_1447'),
        ('teacherApp', '0002_auto_20210712_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentFeedBackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('rating', models.CharField(choices=[('Good', 'Good'), ('Average', 'Average'), ('Bad', 'Bad')], default='none', max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tblclassmodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.coursemodel')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.parentmodel')),
            ],
        ),
    ]