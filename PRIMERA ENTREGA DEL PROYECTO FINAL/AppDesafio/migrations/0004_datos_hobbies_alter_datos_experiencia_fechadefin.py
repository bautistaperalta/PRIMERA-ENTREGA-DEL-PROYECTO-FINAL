# Generated by Django 4.1 on 2022-09-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDesafio', '0003_datos_experiencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbie', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='datos_experiencia',
            name='fechaDefin',
            field=models.DateField(),
        ),
    ]