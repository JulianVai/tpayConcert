# Generated by Django 2.1.3 on 2018-11-15 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20181115_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertickets',
            name='id_event',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordertickets',
            name='order_ip',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordertickets',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordertickets',
            name='state',
            field=models.CharField(max_length=64),
        ),
    ]
