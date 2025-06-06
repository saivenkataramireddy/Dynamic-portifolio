from djongo import models  # Use Djongo's models for MongoDB
from django.contrib.auth.models import AbstractUser
from bson.objectid import ObjectId  # MongoDB ObjectId

class CustomUser(AbstractUser):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",  # Change related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",  # Change related_name to avoid conflict
        blank=True
    )

class Blog(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    name = models.CharField(max_length=400)
    self_introduction = models.FileField(upload_to="images/", blank=True, null=True)
    iam = models.CharField(max_length=500)
    resume = models.FileField(upload_to="images/", blank=True, null=True)
    about_you = models.TextField()
    def __str__(self):
        return self.name if self.name else "Unnamed Blog"
class Skill(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True, null=True)  # e.g., Beginner, Intermediate, Expert
    icon = models.ImageField(upload_to="images/", blank=True, null=True)  # Optional skill icon

    def __str__(self):
        return self.name
class Projects(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.description if self.description else "No description"
    class Meta:
        verbose_name_plural = "Projects"
class Certifications(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description if self.description else "No description"
    class Meta:
        verbose_name_plural = "Certifications"
class Contact(models.Model):
    _id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
