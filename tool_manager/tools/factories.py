import factory
from factory import Faker
import random
from tools.models import Tool
from users.factories import UserFactory


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






