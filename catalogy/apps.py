from django.apps import AppConfig


class CatalogyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "catalogy"

    def ready(self):
        import catalogy.signals
