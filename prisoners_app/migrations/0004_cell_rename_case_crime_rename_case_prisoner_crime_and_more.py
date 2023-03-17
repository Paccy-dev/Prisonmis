# Generated by Django 4.0.4 on 2022-05-29 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prisoners_app', '0003_alter_transfer_where_from_alter_transfer_where_to_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('status', models.IntegerField(default='Empty')),
            ],
        ),
        migrations.RenameModel(
            old_name='Case',
            new_name='Crime',
        ),
        migrations.RenameField(
            model_name='prisoner',
            old_name='case',
            new_name='crime',
        ),
        migrations.RenameField(
            model_name='prisoner',
            old_name='date',
            new_name='entry_date',
        ),
        migrations.AddField(
            model_name='prisoner',
            name='marital_status',
            field=models.TextField(choices=[('1', 'Single'), ('2', 'Married'), ('3', 'Divorced')], default='Single', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitor',
            name='reason',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leave',
            name='approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('1', 'Pending'), ('2', 'Active'), ('3', 'Expired')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='address',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='firstname',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='identification',
            field=models.IntegerField(max_length=16),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='lastname',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='phone',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='status',
            field=models.CharField(choices=[('1', 'INMATE'), ('2', 'OUTMATE')], default='INMATE', max_length=10),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='where_to',
            field=models.TextField(choices=[('1', 'Mageregere'), ('2', 'Muhanga prison'), ('3', 'Ririma prison'), ('4', 'Huye prison'), ('5', 'Nyagatare prison'), ('6', 'Kacyiru'), ('7', 'Wawa')], max_length=20),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='firstname',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='lastname',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='prisoner',
            name='cell',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prisoners_app.cell'),
        ),
    ]