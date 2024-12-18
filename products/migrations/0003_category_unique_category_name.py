# Generated by Django 5.0.3 on 2024-12-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(condition=models.Q(('name__iexact', models.F('name'))), fields=('name',), name='unique_category_name'),
        ),
    ]
