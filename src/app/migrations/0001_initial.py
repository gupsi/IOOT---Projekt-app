# Generated by Django 3.0.7 on 2020-07-09 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazivfirme', models.CharField(blank=True, max_length=500, verbose_name='Naziv firme')),
                ('adresa', models.CharField(blank=True, max_length=30)),
                ('kontakt', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OdradjeniSati',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(auto_now_add=True, null=True)),
                ('pvremena', models.TimeField(blank=True, null=True, verbose_name='Početak radnog vremena')),
                ('kvremena', models.TimeField(blank=True, null=True, verbose_name='Kraj radnog vremena')),
                ('korisnik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Korisnik')),
            ],
            options={
                'verbose_name_plural': 'Odrađeni sati',
            },
        ),
        migrations.CreateModel(
            name='ListaZadataka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('opis', models.TextField(max_length=600)),
                ('status', models.CharField(blank=True, choices=[('u', 'U Tijeku'), ('r', 'Riješeno')], default='u', max_length=1)),
                ('korisnik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Korisnik')),
            ],
            options={
                'verbose_name_plural': 'Kreirani zadaci',
            },
        ),
    ]
