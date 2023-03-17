# Generated by Django 4.0.4 on 2023-03-14 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prisoners_app', '0012_alter_cell_status_alter_prisoner_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('confirmation', models.BooleanField(default=False)),
                ('feedback', models.TextField()),
                ('date', models.DateField()),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisoners_app.prisoner')),
            ],
        ),
    ]