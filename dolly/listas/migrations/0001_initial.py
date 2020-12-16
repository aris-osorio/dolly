# Generated by Django 2.2.14 on 2020-12-15 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tableros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('posicion', models.IntegerField(default=models.AutoField(primary_key=True, serialize=False))),
                ('tablero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tableros.Tablero')),
            ],
        ),
    ]
