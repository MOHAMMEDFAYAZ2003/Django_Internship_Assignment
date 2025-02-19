from django.apps import AppConfig

class SignalsExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals_example'

    def ready(self):
        import signals_example.signals  # ✅ Ensures signals are imported
