# Generated by Django 5.1.3 on 2024-11-22 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attention', '0007_remove_costosatencion_servicios_adicionales_and_more'),
        ('core', '0008_alter_medicamento_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto')),
                ('metodo_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('PayPal', 'PayPal')], max_length=50, verbose_name='Método de Pago')),
                ('pagado', models.BooleanField(default=False, verbose_name='Pagado')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pago')),
                ('costo_atencion', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='attention.costosatencion', verbose_name='Costo Atención')),
                ('examenes_medicos', models.ManyToManyField(blank=True, to='attention.examensolicitado', verbose_name='Examenes Solicitados')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.paciente', verbose_name='Paciente')),
                ('servicios_adicionales', models.ManyToManyField(blank=True, to='attention.serviciosadicionales', verbose_name='Servicios Adicionales')),
            ],
        ),
    ]
