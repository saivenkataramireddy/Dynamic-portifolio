from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Blog, Projects, Certifications, Contact,Skill
from django.core.mail import send_mail

def send_email_to_me(name, email, contact_number, message_text):
    subject = '📩 New Contact Form Submission'
    message = f"""
👤 Name: {name}
📧 Email: {email}
📱 Phone: {contact_number if contact_number else 'N/A'}
💬 Message: {message_text}
"""
    send_mail(
        subject,
        message,
        'yourgmail@gmail.com',  # FROM email
        ['saivenkataramireddykesara@gmail.com'],  # TO email(s)
        fail_silently=False,
    )


# Home Page View
def home(request):
    blogs = Blog.objects.all()
    projects = Projects.objects.all()
    certifications = Certifications.objects.all()
    skills = Skill.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number", "")
        message = request.POST.get("message")

        if name and email and message:
            Contact.objects.create(name=name, email=email, contact_number=contact_number, message=message)
            send_email_to_me(name, email, contact_number, message)  # ✅ Send email
            messages.success(request, "Your message has been sent successfully!")
            return redirect("home")
    return render(request, "index.html", {'blogs': blogs, 'projects': projects, 'certifications': certifications,'skills': skills})


# Robots.txt View
def robots_txt(request):
    content = "User-agent: *\nDisallow: /admin/"
    return HttpResponse(content, content_type="text/plain")
