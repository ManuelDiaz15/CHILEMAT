# Generated by Django 4.2 on 2023-05-11 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AddField(
            model_name='clientes',
            name='Numero',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.RemoveField(
            model_name='venta',
            name='productos',
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='productos',
            field=models.ManyToManyField(through='core.DetalleVenta', to='core.producto'),
        ),
    ]