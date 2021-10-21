# Generated by Django 3.1.7 on 2021-06-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0005_farmersrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomersRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255)),
                ('cphone', models.CharField(max_length=255)),
                ('cadd', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=255)),
                ('fphone', models.CharField(max_length=255)),
                ('fadd', models.CharField(max_length=255)),
                ('crop', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]