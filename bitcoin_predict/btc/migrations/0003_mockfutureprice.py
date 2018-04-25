# Generated by Django 2.0.2 on 2018-04-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btc', '0002_mockprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='MockFuturePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
