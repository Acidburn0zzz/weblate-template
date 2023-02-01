# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.0.5 on 2020-05-15 07:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0077_auto_20200513_1512"),
    ]

    operations = [
        migrations.RemoveField(model_name="unit", name="has_comment"),
        migrations.RemoveField(model_name="unit", name="has_failing_check"),
        migrations.RemoveField(model_name="unit", name="has_suggestion"),
    ]
