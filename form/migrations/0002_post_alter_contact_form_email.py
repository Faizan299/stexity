# Generated by Django 4.0.1 on 2022-01-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('desc', models.TextField()),
                ('image', models.ImageField(default='default.png', upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='contact_form',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
