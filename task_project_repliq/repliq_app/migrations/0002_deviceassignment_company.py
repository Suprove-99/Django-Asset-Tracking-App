# Generated by Django 3.0.7 on 2023-08-23 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repliq_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceassignment',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repliq_app.Company'),
            preserve_default=False,
        ),
    ]
