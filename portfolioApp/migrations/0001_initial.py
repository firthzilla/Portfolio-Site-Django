# Generated by Django 3.2 on 2021-05-13 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('last_edit_date', models.DateTimeField(auto_now=True, verbose_name='last edited')),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('category', models.CharField(choices=[('programming', 'Programming'), ('coding', 'Coding'), ('web development', 'Web Development'), ('python', 'Python'), ('webdev', 'WebDev')], max_length=30)),
                ('description', models.TextField(blank=True)),
                ('coverImage', models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')),
                ('image0', models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')),
                ('image1', models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
