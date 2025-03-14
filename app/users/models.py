import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class User(AbstractUser):
    can_view = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=True)
    can_create = models.BooleanField(default=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ["username"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        self.email = self.email.lower()
        self.username = self.username.lower()
        super(User, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("get-user-detail", kwargs={"slug": self.slug})

    # def __str__(self):
    #     if self.first_name and self.last_name:
    #         return f"{self.first_name} {self.last_name}"
    #     return f"{self.email}"