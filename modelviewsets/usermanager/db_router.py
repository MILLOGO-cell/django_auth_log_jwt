"""
Fichier de routage qui permet de cibler notre schema postgreSQL et d'y generer automatiquement nos tables 
via nos modeles
"""

import models

ROUTED_MODELS = [models.]


class MyDBRouter(object):
    route_app_labels = {'configuration'}

    def db_for_read(self, model, **hints):

        if model in ROUTED_MODELS:
            return 'configuration'

        return None

    def db_for_write(self, model, **hints):

        if model in ROUTED_MODELS:
            return 'configuration'

        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {'configuration'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        if app_label in self.route_app_labels:
            return db == 'configuration'
        return None

    
