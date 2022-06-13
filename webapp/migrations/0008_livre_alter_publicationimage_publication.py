# Generated by Django 4.0.5 on 2022-06-09 07:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_publicationimage_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date_update', models.DateTimeField(default=datetime.datetime(2022, 6, 9, 9, 6, 28, 159534))),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='publicationimage',
            name='publication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='webapp.publication'),
        ),
    ]
