from django.contrib.auth import get_user_model


def create_user(**args):
    """Creates user with the arguments specified"""
    return get_user_model().objects.create_user(**args)


def create_superuser(**args):
    """Creates superuser with the arguments specified"""
    return get_user_model().objects.create_superuser(**args)


def update_superuser(superuser_instance, **superuser_data):
    """Service to update a superuser"""
    [setattr(superuser_instance, attr, value) for attr, value in superuser_data.items()]
    superuser_instance.save()
    return superuser_instance
