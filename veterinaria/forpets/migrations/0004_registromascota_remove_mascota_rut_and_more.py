# Generated by Django 4.0.4 on 2022-06-08 02:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forpets', '0003_remove_atencion_costo_remove_atencion_diagnostico_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='registroMascota',
            fields=[
                ('idMascota', models.IntegerField(primary_key=True, serialize=False, verbose_name='id mascota')),
                ('rutDueno', models.IntegerField(max_length=20, verbose_name='rut del dueño')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre dueño')),
                ('correo', models.CharField(max_length=20, verbose_name='correo dueño')),
                ('nombremascota', models.CharField(max_length=40, verbose_name='nombre mascota')),
                ('edad', models.IntegerField(max_length=10, verbose_name='edad mascota')),
                ('fecha', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='rut',
        ),
        migrations.RemoveField(
            model_name='atencion',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='atencion',
            name='idUsuario',
        ),
        migrations.DeleteModel(
            name='dueno',
        ),
        migrations.DeleteModel(
            name='mascota',
        ),
        migrations.AddField(
            model_name='registromascota',
            name='IdRol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forpets.atencion'),
        ),
    ]
