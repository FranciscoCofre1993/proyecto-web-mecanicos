# Generated by Django 4.2.1 on 2023-07-11 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('snombre', models.CharField(max_length=30)),
                ('apellidop', models.CharField(max_length=30)),
                ('apellidom', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='mecanicos/')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('precio', models.CharField(max_length=30)),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mecanico')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=20)),
                ('anio', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='autos/')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelo')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servicio')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipovehiculo')),
            ],
        ),
    ]
