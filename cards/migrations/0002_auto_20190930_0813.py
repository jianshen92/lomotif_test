# Generated by Django 2.2.5 on 2019-09-30 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("cards", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="cards", old_name="type", new_name="card_type"
        )
    ]