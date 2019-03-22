from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User will be easy to customize in the future."""

    def __str__(self):
        return self.email
