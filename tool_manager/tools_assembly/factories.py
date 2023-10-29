import random

import factory
from factory import Faker

from holders.factories import HolderFactory
from machines.factories import MachineFactory
from tools.factories import ToolFactory
from tools_assembly.models import ToolAssembly, UserComment
from users.factories import UserFactory


class ToolAssemblyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ToolAssembly

    tool_nr = random.randint(1, 100)
    radius = random.uniform(1.0, 30.0)
    total_length = random.uniform(10.0, 485.0)
    outside_holder = random.uniform(5.0, 200.0)
    machine = factory.SubFactory(MachineFactory)
    holder = factory.SubFactory(HolderFactory)
    tool = factory.SubFactory(ToolFactory)
    author = factory.SubFactory(UserFactory)


class UserCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserComment

    content = Faker("text")
    author = factory.SubFactory(UserFactory)
    tool_assembly = factory.SubFactory(ToolAssemblyFactory)
