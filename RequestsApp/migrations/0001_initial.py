# Generated by Django 2.0.3 on 2018-04-01 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interes', models.CharField(choices=[('venta', 'Venta'), ('compra', 'Compra'), ('alquiler', 'Alquiler'), ('remates', 'Remates'), ('administracion', 'Administración'), ('topografia', 'Topografía'), ('asesoramiento', 'Asesoramiento')], max_length=20)),
                ('rubro', models.CharField(choices=[('ganaderia', 'Ganadería'), ('agricultura', 'Agricultura'), ('loteamiento', 'Loteamiento'), ('inversion_inmobiliaria', 'Inversión Inmobiliaria'), ('puerto', 'Puerto'), ('cuenca_aquifera', 'Cuenca Acuifera'), ('residencias', 'Residencias'), ('terrenos', 'Terrenos'), ('otros', 'Otros')], max_length=30)),
                ('zona_preferencia', models.CharField(choices=[('oriental', 'Oriental'), ('occidental', 'Occidental')], max_length=20)),
                ('tamanho', models.CharField(choices=[('0 - 1', '0 - 10.000 m2'), ('1 - 2.5', '10.000 m2 - 25.000 m2'), ('2.5 - 5', '25.000 m2 (2,5 HA)- 5 HA'), ('5 - 10', '5 HA - 10 HA'), ('10 - 20', '10 HA - 20 HA'), ('20 - 50', '20 HA - 50 HA'), ('50 - 100', '50 HA - 100 HA'), ('100 - 300', '100 HA - 300 HA'), ('300 - 600', '300 HA - 600 HA'), ('600 - 2.000', '600 HA - 2.000 HA'), ('2.000 - 5.000', '2.000 HA - 5.000 HA'), ('5.000 - 10.000', '5.000 HA - 10.000 HA'), ('10.000 - *', 'Mayor a 10.000 HA')], max_length=20)),
                ('presupuesto', models.CharField(choices=[('0-10.000', '0 - 10.000 USD'), ('10.000-20.000', '10.000 USD - 20.000 USD'), ('20.000-50.000', '20.000 USD - 50.000 USD'), ('50.000-100.000', '50.000 USD - 100.000 USD'), ('100.000-150.000', '100.000 USD - 150.000 USD'), ('150.000-200.000', '150.000 USD - 200.000 USD'), ('200.000-350.000', '200.000 USD - 350.000 USD'), ('350.000-500.000', '350.000 USD - 500.000 USD'), ('500.000-800.000', '500.000 USD - 800.000 USD'), ('800.000-1.500.000', '800.000 USD - 1.500.000 USD'), ('1.500.000-3.000.000', '1.500.000 USD - 3.000.000 USD'), ('3.000.000-8.000.000', '3.000.000 - 8.000.000 USD'), ('8.000.000-*', 'Mayor a 8.000.000 USD')], max_length=30)),
                ('formacion', models.CharField(choices=[('formado', 'Formado'), ('semi-formado', 'Semi Formado'), ('a-formar', 'A Formar')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=20)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('nro_telefono', models.CharField(max_length=20)),
                ('ocupacion', models.CharField(max_length=20)),
                ('idioma', models.CharField(choices=[('esp', 'Español'), ('ing', 'Inglés'), ('por', 'Portugués'), ('ale', 'Alemán'), ('fra', 'Francés')], max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RequestsApp.Usuario'),
        ),
    ]
