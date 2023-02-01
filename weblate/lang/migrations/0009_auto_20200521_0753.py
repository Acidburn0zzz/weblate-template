# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.6 on 2020-05-21 07:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lang", "0008_auto_20200408_0436"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="language",
            options={
                "base_manager_name": "objects",
                "verbose_name": "Language",
                "verbose_name_plural": "Languages",
            },
        ),
    ]
