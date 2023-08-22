# Generated by Django 2.2.24 on 2021-11-08 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0054_auto_20211017_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='OctoPrintTunnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.TextField()),
                ('subdomain_code', models.TextField(blank=True, null=True, unique=True)),
                ('basicauth_username', models.TextField(blank=True, null=True)),
                ('basicauth_password', models.TextField(blank=True, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Printer')),
            ],
        ),
    ]
