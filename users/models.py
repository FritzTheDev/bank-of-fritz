from django.db.models import EmailField
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
  email = EmailField(unique=True, max_length=100)

  USERNAME_FIELD = 'email'