import factory
from django.contrib.auth.models import User
from factory import Faker

from users.models import Profile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("user_name")
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    password = factory.PostGenerationMethodCall("set_password", "testpassword")


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
