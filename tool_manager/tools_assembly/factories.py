import factory
from factory import Faker
import random
from tools_assembly.models import Holder, Tool, ToolAssembly, UserComment
from machines.factories import MachineFactory
from users.factories import UserFactory


class HolderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Holder

    holder_type = factory.LazyFunction(lambda: random.choice([choice[0] for choice in Holder.holder_type_choices]))
    inner_diameter = random.randint(1, 25)
    catalog_nr = Faker('word')
    LH1 = random.uniform(20.0, 150.0)
    DH1_A = random.uniform(25.0, 30.0)
    DH1_B = random.uniform(30.0, 40.0)
    LH2 = random.uniform(1.0, 10.0)
    DH2 = random.uniform(40.0, 50.0)
    LH3 = random.uniform(1.0, 26.0)
    DH3 = random.uniform(50.0, 63.0)
    author = factory.SubFactory(UserFactory)


class ToolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tool

    tool_type = factory.LazyFunction(lambda: random.choice([choice[0] for choice in Tool.tool_type_choices]))
    catalog_nr = Faker('word')
    R = random.uniform(1, 10)
    L1 = random.uniform(1.0, 250.0)
    D1 = random.uniform(1.0, 30.0)
    L2 = random.uniform(1.0, 10.0)
    D2 = random.uniform(1.0, 25.0)
    L3 = random.uniform(1.0, 10.0)
    D3 = random.uniform(1.0, 25.0)
    L4 = random.uniform(1.0, 10.0)
    D4 = random.uniform(1.0, 25.0)
    author = factory.SubFactory(UserFactory)


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

    content = Faker('text')
    author = factory.SubFactory(UserFactory)
    toolassembly = factory.SubFactory(ToolAssemblyFactory)





