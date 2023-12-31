import factory
from factory import Faker

from notifications.models import Notification, UserNotification
from tools_assembly.factories import UserCommentFactory
from users.factories import UserFactory


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    user = factory.SubFactory(UserFactory)

    user_comment = factory.SubFactory(UserCommentFactory)
    message = Faker("text")


class UserNotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserNotification

    user = factory.SubFactory(UserFactory)
    notification = Faker("text")
