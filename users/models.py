from django.db.models import EmailField, BooleanField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not email:
            raise ValueError('Error: The User you want to create must have an email, try again')

        user = self.model(email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given username and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
  email = EmailField(unique=True, max_length=100)
  is_staff = BooleanField(default=False)
  is_admin = BooleanField(default=False)
  objects = UserManager()

  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'