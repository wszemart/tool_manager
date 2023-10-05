from django.apps import AppConfig
from django.dispatch import receiver
from django.db.models.signals import post_migrate



class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals

        post_migrate.connect(self._create_groups_and_permissions, sender=self)

    def _create_groups_and_permissions(self, sender, **kwargs):
        from django.contrib.auth.models import Group, Permission
        operator, created = Group.objects.get_or_create(name='Operator')
        programmer, created = Group.objects.get_or_create(name='Programmer')

        permissions_operator = Permission.objects.filter(codename__in=[
            'view_profile',
            'change_profile',
            'view_machine',
            'view_holder',
            'view_tool',
            'change_toolassembly',
            'view_toolassembly',
            'add_usercomment',
            'change_usercomment',
            'delete_usercomment',
            'view_usercomment',
            'add_notification',
            'change_notification',
            'delete_notification',
            'view_notification',
            'add_usernotification',
            'change_usernotification',
            'delete_usernotification',
            'view_usernotification',
        ]).values_list('id', flat=True)
        print(permissions_operator)
        permissions_programmer = Permission.objects.filter(codename__in=[
            'add_machine',
            'change_machine',
            'delete_machine',
            'view_machine',
            'add_profile',
            'change_profile',
            'delete_profile',
            'view_profile',
            'add_holder',
            'change_holder',
            'delete_holder',
            'view_holder',
            'add_tool',
            'change_tool',
            'delete_tool',
            'view_tool',
            'add_toolassembly',
            'change_toolassembly',
            'delete_toolassembly',
            'view_toolassembly',
            'add_usercomment',
            'change_usercomment',
            'delete_usercomment',
            'view_usercomment',
            'add_notification',
            'change_notification',
            'delete_notification',
            'view_notification',
            'add_usernotification',
            'change_usernotification',
            'delete_usernotification',
            'view_usernotification',
        ]).values_list('id', flat=True)
        print(permissions_programmer)
        operator.permissions.add(*permissions_operator)
        programmer.permissions.add(*permissions_programmer)
