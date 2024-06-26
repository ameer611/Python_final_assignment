# Generated by Django 5.0.2 on 2024-05-07 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=28)),
                ('position', models.CharField(choices=[('director', 'Director'), ('marketing_manager', 'Marketing Manager'), ('selles_manager', 'Selles Manager'), ('hr', 'HR')], max_length=60)),
                ('staff_image', models.ImageField(blank=True, null=True, upload_to='staffes_images/')),
            ],
        ),
    ]
