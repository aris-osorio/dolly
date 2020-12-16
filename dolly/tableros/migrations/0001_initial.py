# Generated by Django 2.2.14 on 2020-12-15 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tablero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('favorito', models.BooleanField(default=False)),
                ('visibilidad', models.CharField(max_length=200)),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Usuario')),
                ('miembros', models.ManyToManyField(related_name='tableros', to='usuarios.Usuario')),
            ],
        ),
    ]