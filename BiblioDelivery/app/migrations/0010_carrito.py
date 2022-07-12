# Generated by Django 4.0.4 on 2022-07-08 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_producto_stockproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadCarrito', models.IntegerField()),
                ('tiempoCarrito', models.DateTimeField(auto_now_add=True)),
                ('productoCarrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
                ('userCarrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
    ]