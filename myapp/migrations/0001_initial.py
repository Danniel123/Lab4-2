# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=15)),
                ('Age', models.CharField(max_length=15)),
                ('Country', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=30)),
                ('Publisher', models.CharField(max_length=20)),
                ('PublishDate', models.DateField()),
                ('Price', models.CharField(max_length=10)),
                ('AuthorID', models.ForeignKey(to='myapp.Author')),
            ],
        ),
    ]
