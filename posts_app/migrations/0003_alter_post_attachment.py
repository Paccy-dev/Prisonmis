# Generated by Django 4.0.4 on 2022-05-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0002_alter_post_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='attachment',
            field=models.FileField(null=True, upload_to='docs/'),
        ),
    ]