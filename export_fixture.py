# export_fixture.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.core.management import call_command

with open("catalogy/fixtures/catalog_data.json", "w", encoding="utf-8") as f:
    call_command(
        "dumpdata",
        "catalogy.Category",
        "catalogy.Product",
        indent=4,
        stdout=f
    )
