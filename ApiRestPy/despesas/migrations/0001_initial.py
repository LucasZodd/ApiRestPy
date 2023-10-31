# Generated by Django 4.2.6 on 2023-10-31 01:44

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
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_nome', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('despesa_id', models.AutoField(primary_key=True, serialize=False)),
                ('despesa_descricao', models.TextField(default='')),
                ('despesa_data', models.DateField(default='')),
                ('despesa_valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('despesa_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='despesas.categoria')),
            ],
        ),
    ]
