# Generated by Django 5.2.3 on 2025-07-11 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_help', '0004_task_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='SME',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sme_tasks', to='online_help.writers'),
        ),
    ]
