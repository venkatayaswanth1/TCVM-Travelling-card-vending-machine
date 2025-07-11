# Generated by Django 5.0.3 on 2024-04-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_alter_customer_user_remove_customer_confirmpassword_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='cardid',
            field=models.CharField(default='not issued', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
