# Generated by Django 5.0.7 on 2024-07-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0003_alter_workituser_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='workituser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]