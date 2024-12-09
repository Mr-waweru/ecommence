from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    """how to create a regular user"""
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email) # Ensures the email is in a standard format
        user = self.model(email=email)  # Creates a user instance using the custom user model
        user.set_password(password) # Hashes the password for security
        user.save(using=self._db)   # Saves the user to the database
        return user

    """Defines how to create a superuser (admin user)"""
    def create_superuser(self, email, password):
        user = self.create_user(email, password)    # Calls create_user to create the user instance
        user.is_staff = True    # Sets is_staff flag to True to grant admin privileges
        user.is_superuser = True    # Sets is_superuser flags to True to grant admin privileges
        user.save(using=self.db)
        return user

"""
User inherits from AbstractUser, which provides all the default fields and
functionality for a user (e.g., username, email, password, groups, permissions).
"""
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=10, unique=True)

    USERNAME_FIELD = "email"    # Specifies email as the unique identifier for authentication instead of the default username
    REQUIRED_FIELDS = []    # Left empty here, meaning only email and password are mandatory.
    objects = UserManager() # Associates the custom UserManager class with this model, enabling the use of create_user and create_superuser methods.