# Generated by Django 4.0.4 on 2022-05-24 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformer',
            name='consecutive_months_overloaded',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='customers',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='date_max_overload',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='life_expectancy_at_conditions',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='loading_flags',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='loss_of_life',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='max_overload',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='percent_lol',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='size_kva',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transformer',
            name='transformer_age',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
