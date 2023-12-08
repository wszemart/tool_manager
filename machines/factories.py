import factory
from factory import Faker

from machines.models import Machine


class MachineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Machine

    name = Faker("word")
    description = Faker("text")
