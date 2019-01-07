# Generated by Django 2.1 on 2018-08-18 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ameneties',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pg'),
        ),
        migrations.AlterField(
            model_name='contactowner',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pg'),
        ),
        migrations.AlterField(
            model_name='contactowner',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pg'),
        ),
        migrations.AlterField(
            model_name='favourites',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
        migrations.AlterField(
            model_name='pg',
            name='ownerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.owner'),
        ),
        migrations.AlterField(
            model_name='pgimages',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pg'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='pgid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pg'),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
    ]