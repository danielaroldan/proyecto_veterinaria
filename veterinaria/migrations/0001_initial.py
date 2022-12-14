# Generated by Django 3.2.16 on 2022-10-28 12:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import veterinaria.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('articulo', models.AutoField(primary_key=True, serialize=False)),
                ('codigoArticulo', models.IntegerField()),
                ('precioArticulo', models.IntegerField()),
                ('detalleArticulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('razonSocialCliente', models.CharField(max_length=200)),
                ('direccionCliente', models.CharField(max_length=200)),
                ('localidadCliente', models.CharField(max_length=200)),
                ('provinciaCliente', models.CharField(max_length=200)),
                ('codigoPostalCliente', models.CharField(max_length=10)),
                ('telefonoCliente', models.CharField(max_length=20)),
                ('ivaCliente', models.BooleanField()),
                ('mailCliente', models.CharField(max_length=200)),
                ('fechaCreacionCliente', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaModificaciÃ³nCliente', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaBajaCliente', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='StockArticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entradaStock', models.IntegerField()),
                ('salidaStock', models.IntegerField()),
                ('stockArticulo', models.IntegerField()),
                ('fechaCreacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaModificaciÃ³n', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaBaja', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadTotalArticulo', models.IntegerField()),
                ('precioUnitarioArticulo', models.IntegerField()),
                ('fechaVenta', models.DateTimeField(default=django.utils.timezone.now)),
                ('cantidadUnitarioArticulo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock_artic', to='veterinaria.stockarticulo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='veterinaria.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaFactura', models.DateTimeField(default=django.utils.timezone.now)),
                ('precioUnitarioArticulo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('precioTotalArticulo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=8)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aticulo', to='veterinaria.articulo')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factura', to='veterinaria.cliente')),
                ('venta', models.OneToOneField(default=veterinaria.models.Venta, on_delete=django.db.models.deletion.CASCADE, to='veterinaria.venta')),
            ],
        ),
    ]
