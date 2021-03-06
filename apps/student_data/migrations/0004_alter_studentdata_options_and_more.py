# Generated by Django 4.0.1 on 2022-02-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_data', '0003_alter_studentdata_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentdata',
            options={'ordering': ['-rating'], 'verbose_name': 'Student Data', 'verbose_name_plural': 'Student Data'},
        ),
        migrations.AddField(
            model_name='studentdata',
            name='dr_rashids_notes',
            field=models.TextField(blank=True, null=True, verbose_name="Dr. Rashid's Notes"),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Rating'),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Default'), (1, 'Package Sent'), (2, 'Converted'), (3, 'Follow-up'), (4, 'Muted')], default=0, verbose_name='Status'),
        ),
    ]
