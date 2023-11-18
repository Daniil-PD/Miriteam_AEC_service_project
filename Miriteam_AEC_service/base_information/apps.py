from django.apps import AppConfig


class BaseInformationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_information'
