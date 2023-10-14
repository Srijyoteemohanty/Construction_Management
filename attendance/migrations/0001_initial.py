# Generated by Django 4.2.6 on 2023-10-13 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workforce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workforce.workforce')),
            ],
        ),
    ]