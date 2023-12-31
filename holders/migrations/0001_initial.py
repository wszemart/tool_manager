# Generated by Django 4.2.3 on 2023-09-30 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Holder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_type', models.CharField(choices=[('type_1', 'SLIM_100'), ('type_2', 'SLIM_150'), ('type_3', 'SLIM_200'), ('type_4', 'TERMO_100'), ('type_5', 'TERMO_150'), ('type_6', 'TERMO_200'), ('type_7', 'ER_32'), ('type_8', 'ER_40'), ('type_9', 'WELDON_100'), ('type_10', 'WELDON_150'), ('type_11', 'WELDON_200'), ('type_12', 'STYROPIAN'), ('type_13', 'UCHWYT_76')], max_length=100)),
                ('inner_diameter', models.PositiveIntegerField()),
                ('catalog_nr', models.CharField(blank=True, max_length=100)),
                ('LH1', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('DH1_A', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('DH1_B', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('LH2', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('DH2', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('LH3', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('DH3', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
