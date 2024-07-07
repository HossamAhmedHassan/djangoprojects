from django.apps import AppConfig
# TODO: what is the purpose of suit.apps import DjangoSuitConfig, I didn't find any usage for it
from suit.apps import DjangoSuitConfig

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'