# Generated by Django 3.1.6 on 2021-05-20 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_auto_20210520_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientfeedbackmodel',
            name='client',
        ),
        migrations.RemoveField(
            model_name='clientfeedbackmodel',
            name='course',
        ),
        migrations.RemoveField(
            model_name='complaintmodel',
            name='student',
        ),
        migrations.RemoveField(
            model_name='submitclientcomplainmodel',
            name='complain_id',
        ),
        migrations.DeleteModel(
            name='ClientComplainModel',
        ),
        migrations.DeleteModel(
            name='ClientFeedBackModel',
        ),
        migrations.DeleteModel(
            name='ComplaintModel',
        ),
        migrations.DeleteModel(
            name='SubmitClientComplainModel',
        ),
    ]
