from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async

from app.repo.models import Repo

from app.user.tasks import get_repo


def __str__(self):
    return '%s  %s  %s  %d' % (self.date, self.method, self.status, self.amount)


class UserManager(BaseUserManager):
    def create_user(self, full_name, email, password=None, git_token=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not full_name:
            raise ValueError('Users must have full name.')

        user = self.model(
            full_name=full_name,
            email=self.normalize_email(email),
            git_token=git_token
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, email, password, git_token):
        """
        Creates and saves a superuser with the given full name, email and password.
        """
        user = self.create_user(
            full_name,
            email,
            password=password,
            git_token=git_token
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    git_token = models.CharField(_("Git token"), max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'full_name'
    REQUIRED_FIELDS = ['email', 'git_token']

    def get_full_name(self):
        # The user is identified by their Full Name
        return self.full_name

    def get_short_name(self):
        # The user is identified by their Full Name
        return self.full_name

    def __str__(self):  # __unicode__ on Python 2
        return self.full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

        # @property
        # def is_staff(self):
        #     "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        # return self.is_admin

    @property
    def is_superuser(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


@receiver(post_save, sender=User, dispatch_uid="update_repo_meta_count")
def get_repo_meta(sender, instance, **kwargs):
    async(get_repo, instance)
