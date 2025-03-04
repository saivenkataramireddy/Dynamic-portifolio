from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Blog, Projects, Certifications, Contact

# Home Page View
def home(request):
    blogs = Blog.objects.all()
    projects = Projects.objects.all()
    certifications = Certifications.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number", "")
        message = request.POST.get("message")

        if name and email and message:
            Contact.objects.create(name=name, email=email, contact_number=contact_number, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect("home")  # Redirect to home after successful form submission

    return render(request, "index.html", {'blogs': blogs, 'projects': projects, 'certifications': certifications})


# Robots.txt View
def robots_txt(request):
    content = "User-agent: *\nDisallow: /admin/"
    return HttpResponse(content, content_type="text/plain")
