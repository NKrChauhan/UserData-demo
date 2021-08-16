# Generated by Django 3.2.6 on 2021-08-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=120)),
                ('l_name', models.CharField(max_length=120)),
                ('s_name', models.CharField(max_length=120)),
                ('title_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('contact_ext', models.CharField(max_length=4)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('picture_lg', models.URLField(blank=True, null=True)),
                ('picture_md', models.URLField(blank=True, null=True)),
                ('picture_sm', models.URLField(blank=True, null=True)),
                ('team', models.CharField(max_length=120)),
                ('job_title', models.CharField(max_length=120)),
                ('logged_in', models.BooleanField(default=False)),
                ('last_logged', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
