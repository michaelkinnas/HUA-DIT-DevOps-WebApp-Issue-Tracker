from django.apps import AppConfig
from django.db.models.signals import post_migrate, pre_migrate


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'   
   
    def ready(self):
        from .signals import createGroupsAndPermissions
        from .signals import createTestUsers
        
        post_migrate.connect(createGroupsAndPermissions, sender=self)
        post_migrate.connect(createTestUsers, sender=self)