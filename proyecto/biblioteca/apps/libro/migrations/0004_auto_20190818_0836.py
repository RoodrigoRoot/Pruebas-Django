# Generated by Django 2.2.4 on 2019-08-18 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Author'),
        ),
    ]