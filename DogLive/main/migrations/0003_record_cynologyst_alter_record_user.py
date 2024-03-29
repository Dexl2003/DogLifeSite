# Generated by Django 4.2.2 on 2023-06-14 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_price_date_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='cynologyst',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='user', to='main.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.user'),
        ),
    ]
