# Generated by Django 5.1.2 on 2024-10-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Panne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_signalement', models.DateTimeField(auto_now_add=True)),
                ('localisation', models.CharField(max_length=255)),
                ('etat', models.CharField(choices=[('Signalée', 'Signalée'), ('En cours', 'En cours'), ('Résolue', 'Résolue')], default='Signalée', max_length=50)),
            ],
        ),
    ]
