import factory
from factory import Faker
from notifications.models import Notification, UserNotification
from users.factories import UserFactory
from tools_assembly.factories import UserCommentFactory


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    user = UserFactory()
    user_comment = UserCommentFactory()
    message = Faker('text')


class UserNotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserNotification

    user = UserFactory()
    notification = Faker('text')

