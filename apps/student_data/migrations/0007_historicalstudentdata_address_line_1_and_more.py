# Generated by Django 4.0.1 on 2022-03-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_data', '0006_studentprogress_historicalstudentprogress'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalstudentdata',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='historicalstudentdata',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='historicalstudentdata',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='historicalstudentdata',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='historicalstudentdata',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='historicalstudentdata',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='historicalstudentdata',
            name='marital_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Marital Status'),
        ),
        migrations.AddField(
            model_name='historicalstudentdata',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='historicalstudentdata',
            name='zip_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Zip Code'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='marital_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Marital Status'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='zip_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Zip Code'),
        ),
    ]
