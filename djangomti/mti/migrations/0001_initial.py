# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePlugin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subscription_id', models.AutoField(serialize=False, primary_key=True)),
                ('send_emails', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleSubscription',
            fields=[
                ('subscription_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='mti.Subscription')),
                ('articleplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mti.ArticlePlugin')),
            ],
            bases=('mti.articleplugin', 'mti.subscription'),
        ),
    ]
