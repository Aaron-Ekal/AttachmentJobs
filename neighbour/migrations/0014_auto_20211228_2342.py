# Generated by Django 2.2.24 on 2021-12-28 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0013_profile_neighbourhood'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='neighbourhood',
            options={'ordering': ['-pk']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='hood',
            new_name='neighbourhood',
        ),
    ]
