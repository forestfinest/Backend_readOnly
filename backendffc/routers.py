class AccountRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'User'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to accounts.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'accounts'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to accounts.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'accounts'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'accounts' database.
        """
        if app_label in self.route_app_labels:
            return db == 'accounts'
        return None

class DataRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'gis_api'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to accounts.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'data'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to accounts.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'data'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'accounts' database.
        """
        if app_label in self.route_app_labels:
            return db == 'data'
        return None