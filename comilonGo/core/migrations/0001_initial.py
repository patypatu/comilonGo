# Generated by Django 4.0.5 on 2022-07-05 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('descripcion', models.CharField(max_length=20, verbose_name='Descripcion')),
                ('precio', models.CharField(max_length=12, verbose_name='Precio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]