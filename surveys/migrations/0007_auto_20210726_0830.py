# Generated by Django 3.2.5 on 2021-07-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0006_alter_answer_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choices',
        ),
        migrations.AddField(
            model_name='answer',
            name='choices',
            field=models.ManyToManyField(blank=True, null=True, related_name='answer', to='surveys.Choice'),
        ),
    ]
