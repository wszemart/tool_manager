# Generated by Django 4.2.3 on 2023-08-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools_assembly', '0002_tool_r_alter_tool_tool_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='D1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='D2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='D3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='D4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='L1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='L2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='L3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='L4',
            field=models.FloatField(blank=True, null=True),
        ),
    ]