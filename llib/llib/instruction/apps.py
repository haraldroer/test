from django.apps import AppConfig
import analytics
class MyAppConfig(AppConfig):

    def ready(self):
        analytics.write_key = 'YOUR_WRITE_KEY'


class InstructionConfig(AppConfig):
    name = 'instruction'
