# Generated by Django 4.2.1 on 2023-06-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0002_alter_issue_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
    ]
