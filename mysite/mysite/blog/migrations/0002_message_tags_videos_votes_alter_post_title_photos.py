# Generated by Django 4.1.7 on 2023-06-20 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('mag_Id', models.AutoField(primary_key=True, serialize=False)),
                ('mag_AdminId', models.IntegerField()),
                ('mag_title', models.CharField(max_length=150)),
                ('mag_user', models.CharField(max_length=50)),
                ('mag_content', models.TextField()),
                ('addDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_Id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_Name', models.CharField(max_length=50)),
                ('tag_Dee', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('vdeos_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Admin_Id', models.IntegerField()),
                ('vdeos_Name', models.CharField(max_length=50)),
                ('vdeos_Des', models.CharField(max_length=500)),
                ('vdeos_Url', models.TextField()),
                ('addDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('vote_ID', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('photo_Id', models.AutoField(primary_key=True, serialize=False)),
                ('photo_name', models.CharField(max_length=50)),
                ('photo_intro', models.CharField(max_length=200)),
                ('photo_Url', models.CharField(max_length=50)),
                ('addDate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
