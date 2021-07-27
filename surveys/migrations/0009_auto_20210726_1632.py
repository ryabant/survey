# Generated by Django 3.2.5 on 2021-07-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0008_alter_answer_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='survey',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]