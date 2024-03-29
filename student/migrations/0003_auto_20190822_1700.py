# Generated by Django 2.2.4 on 2019-08-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190822_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cgpa',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projects',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='roll_no',
            field=models.CharField(default='', max_length=20),
        ),
    ]
