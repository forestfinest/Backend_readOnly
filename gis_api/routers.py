from .models import project_area

ROUTED_MODELS = [project_area]

class DataRouter(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'samples'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'samples'
        return None