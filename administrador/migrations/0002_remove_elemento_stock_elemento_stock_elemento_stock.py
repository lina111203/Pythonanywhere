# Generated by Django 4.0.3 on 2022-06-08 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elemento',
            name='stock',
        ),
        migrations.AddField(
            model_name='elemento',
            name='stock_elemento',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha de Registro')),
                ('stock_agregada', models.IntegerField(default=0, verbose_name='Stock Nuevo')),
                ('stock_stock', models.IntegerField(verbose_name='Stock')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Anulado', 'Anulado')], default='Activo', max_length=10, verbose_name='Estado')),
                ('elemento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.elemento', verbose_name='elemento')),
            ],
        ),
    ]
