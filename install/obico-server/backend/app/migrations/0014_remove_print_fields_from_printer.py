# Generated by Django 2.1.7 on 2019-05-18 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_add_alert_fields_to_print'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalprinter',
            name='alert_acknowledged_at',
        ),
        migrations.RemoveField(
            model_name='historicalprinter',
            name='current_print_alerted_at',
        ),
        migrations.RemoveField(
            model_name='historicalprinter',
            name='current_print_filename',
        ),
        migrations.RemoveField(
            model_name='historicalprinter',
            name='current_print_started_at',
        ),
        migrations.RemoveField(
            model_name='historicalprinter',
            name='print_status_updated_at',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='alert_acknowledged_at',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='current_print_alerted_at',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='current_print_filename',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='current_print_started_at',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='print_status_updated_at',
        ),
    ]
