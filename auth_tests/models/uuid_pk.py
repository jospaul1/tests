import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tests.custom_user import RemoveGroupsAndPermissions
from django.db import models

with RemoveGroupsAndPermissions():
    class UUIDUser(AbstractUser):
        """A user with a UUID as primary key"""
        myuuid=uuid.uuid4().__str__()
        id = models.UUIDField(default=myuuid, primary_key=True)

        class Meta:
            app_label = 'auth'
