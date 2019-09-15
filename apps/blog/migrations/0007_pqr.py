# Generated by Django 2.2.4 on 2019-09-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190819_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='PQR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=150, verbose_name='Correo Electrónico')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('mensaje', models.TextField(max_length=1000, verbose_name='Mensaje')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacíon')),
            ],
            options={
                'verbose_name': 'Peticiones, Quejas y/o Reclamos',
                'verbose_name_plural': 'Peticiones, Quejas y/o Reclamos',
            },
        ),
    ]