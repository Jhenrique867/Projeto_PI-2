<<<<<<< HEAD
# Generated by Django 5.1.1 on 2024-11-05 20:38
=======
# Generated by Django 5.1.2 on 2024-11-06 18:49
>>>>>>> 412b564798e7fa0dbdbda709840ec3c9daf10a1d

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.AutoField(primary_key=True, serialize=False)),
<<<<<<< HEAD
=======
                ('nome', models.TextField(max_length=100)),
>>>>>>> 412b564798e7fa0dbdbda709840ec3c9daf10a1d
                ('descricao', models.TextField(max_length=100)),
                ('quantidade', models.IntegerField(max_length=4)),
                ('fornecedor', models.TextField(max_length=100)),
                ('marca', models.TextField(max_length=255)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_produto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lucro', models.DecimalField(decimal_places=2, max_digits=5)),
<<<<<<< HEAD
                ('observação', models.TextField(max_length=255)),
=======
                ('observacao', models.TextField(max_length=255)),
>>>>>>> 412b564798e7fa0dbdbda709840ec3c9daf10a1d
            ],
        ),
    ]