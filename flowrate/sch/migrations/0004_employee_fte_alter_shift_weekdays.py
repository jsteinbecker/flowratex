# Generated by Django 4.1.5 on 2023-01-28 07:31

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0003_slot_employee_alter_shift_weekdays'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='fte',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shift',
            name='weekdays',
            field=multiselectfield.db.fields.MultiSelectField(default=[0, 1, 2, 3, 4, 5, 6], max_length=14, verbose_name=((0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'))),
        ),
    ]
