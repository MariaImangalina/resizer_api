# Generated by Django 4.2.3 on 2023-07-03 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('filename', models.CharField(blank=True, verbose_name='Название файла')),
            ],
        ),
        migrations.CreateModel(
            name='ResizedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='resized_images', verbose_name='Изображение')),
                ('width', models.IntegerField(verbose_name='Ширина изображения')),
                ('height', models.IntegerField(null=True, verbose_name='Высота изображения')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resized_images', to='image.image')),
            ],
        ),
    ]
