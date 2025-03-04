from django.contrib import admin, messages
from bson import ObjectId
from .models import Blog, Projects, Contact, Certifications

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("name", "iam", "image")
    search_fields = ("name", "iam")

    def delete_model(self, request, obj):
        """Ensure the object is deleted from MongoDB"""
        obj.delete()
        messages.success(request, "Blog deleted successfully!")

    def has_delete_permission(self, request, obj=None):
        """Ensure delete permission is enabled."""
        return True

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("description", "image")
    search_fields = ("description",)

    def delete_model(self, request, obj):
        """Ensure project is deleted from MongoDB"""
        obj.delete()
        messages.success(request, "Project deleted successfully!")

@admin.register(Certifications)
class CertificationsAdmin(admin.ModelAdmin):
    list_display = ("image", "description")
    search_fields = ("description",)

    def delete_model(self, request, obj):
        """Ensure certification is deleted from MongoDB"""
        obj.delete()
        messages.success(request, "Certification deleted successfully!")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "contact_number", "message", "created_at")
    search_fields = ("name", "email", "contact_number")

    def delete_model(self, request, obj):
        """Ensure contact is deleted from MongoDB"""
        obj.delete()
        messages.success(request, "Contact deleted successfully!")

    def has_delete_permission(self, request, obj=None):
        """Allow deletion of contact messages"""
        return True
