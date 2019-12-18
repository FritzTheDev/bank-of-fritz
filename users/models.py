from django.db.models import EmailField
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Error: The User you want to create must have an email, try again')

        user = self.model(
            user=self.normalize_username(username),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
  email = EmailField(unique=True, max_length=100)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'