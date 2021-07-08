# Generated by Django 3.2.4 on 2021-07-07 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_auto_20210707_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=40, on_delete=django.db.models.deletion.PROTECT, related_name='clasificacion_categoria', to='APP.categoria'),
            preserve_default=False,
        ),
    ]