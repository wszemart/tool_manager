import random

import factory
from factory import Faker

from holders.models import Holder
from users.factories import UserFactory


class HolderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Holder

    holder_type = factory.LazyFunction(lambda: random.choice([choice[0] for choice in Holder.holder_type_choices]))
    inner_diameter = random.randint(1, 25)
    catalog_nr = Faker("word")
    LH1 = random.uniform(20.0, 150.0)
    DH1_A = random.uniform(25.0, 30.0)
    DH1_B = random.uniform(30.0, 40.0)
    LH2 = random.uniform(1.0, 10.0)
    DH2 = random.uniform(40.0, 50.0)
    LH3 = random.uniform(1.0, 26.0)
    DH3 = random.uniform(50.0, 63.0)
    author = factory.SubFactory(UserFactory)
