# Generated by Django 2.2.4 on 2019-08-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['nombre'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='author',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
