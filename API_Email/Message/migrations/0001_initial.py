# Generated by Django 5.0.4 on 2024-04-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(blank=True, default='yash.avasekar.1999@gmail.com', max_length=254, null=True)),
                ('receiver', models.TextField()),
                ('subject', models.CharField(default='', max_length=100)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]