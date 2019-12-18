from django.db.models import EmailField
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractBaseUser):
  email = EmailField(max_length=100, unique=True)

  USERNAME_FIELD = 'email'
