# Generated by Django 3.1.1 on 2020-09-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('genre', models.CharField(choices=[('feminin', 'Feminin'), ('masculin', 'Masculin')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
