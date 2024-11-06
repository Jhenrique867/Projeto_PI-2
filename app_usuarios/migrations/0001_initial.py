# Generated by Django 5.1.1 on 2024-11-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_usuario', models.TextField(max_length=255)),
                ('sobrenome_usuario', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
