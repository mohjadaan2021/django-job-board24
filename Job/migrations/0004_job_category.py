# Generated by Django 4.2.14 on 2024-07-29 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0003_categroy'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Job.categroy'),
            preserve_default=False,
        ),
    ]
