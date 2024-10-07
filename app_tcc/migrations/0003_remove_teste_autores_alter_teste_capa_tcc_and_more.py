# Generated by Django 5.1.1 on 2024-10-07 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tcc', '0002_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teste',
            name='autores',
        ),
        migrations.AlterField(
            model_name='teste',
            name='capa_tcc',
            field=models.FileField(default='', upload_to='capas/'),
        ),
        migrations.AlterField(
            model_name='teste',
            name='orientador',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teste',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='teste',
            name='autores',
            field=models.TextField(default=''),
        ),
    ]
