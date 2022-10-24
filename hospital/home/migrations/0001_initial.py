# Generated by Django 4.1.2 on 2022-10-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=20)),
                ('doc_description', models.TextField()),
                ('doc_image', models.ImageField(upload_to='doctors')),
            ],
        ),
    ]