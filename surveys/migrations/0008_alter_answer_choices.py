# Generated by Django 3.2.5 on 2021-07-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0007_auto_20210726_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choices',
            field=models.ManyToManyField(blank=True, related_name='answer', to='surveys.Choice'),
        ),
    ]
