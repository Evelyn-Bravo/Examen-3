# Generated by Django 5.2 on 2025-05-07 03:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_producto_categoria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('metodo_pago', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta'), ('transferencia', 'Transferencia')], max_length=20)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('procesando', 'Procesando'), ('enviado', 'Enviado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='producto',
        ),
        migrations.AddField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='codigo_postal',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('arreglo floral', 'Arreglo Floral'), ('ramo de flores', 'Ramo de Flores'), ('jarrones', 'Jarrones')], max_length=50),
        ),
        migrations.AddField(
            model_name='cart',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.cliente'),
        ),
        migrations.AddField(
            model_name='cart',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.cliente'),
        ),
        migrations.AddField(
            model_name='pedidoitem',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tasks.pedido'),
        ),
        migrations.AddField(
            model_name='pedidoitem',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.producto'),
        ),
        migrations.DeleteModel(
            name='ItemCarrito',
        ),
        migrations.DeleteModel(
            name='Orden',
        ),
    ]
