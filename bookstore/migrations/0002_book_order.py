# Generated by Django 5.0.2 on 2024-02-26 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, null=True)),
                ('author', models.CharField(max_length=190, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Classics', 'Classics'), ('Commic Book', 'Comic Book'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror')], max_length=200, null=True)),
                ('description', models.CharField(max_length=190, null=True)),
                ('date_created', models.DateTimeField(max_length=190, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(max_length=190, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delevered', 'Delevered'), ('in progress', 'in progress'), ('out of order', 'out of order')], max_length=200, null=True)),
            ],
        ),
    ]
