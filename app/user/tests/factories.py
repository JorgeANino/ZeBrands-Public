from uuid import uuid4

import factory

from user.models import CatalogUser


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CatalogUser

    email = factory.LazyAttributeSequence(lambda o, n: f"{uuid4()}@zebrands.com")
    is_active = True

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted if extracted else "test123"
        self.set_password(password)
        self.save()
        self.password_plain_text = password

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        self.save()
        if not create:
            return

        if extracted:
            self.groups.set(extracted)
