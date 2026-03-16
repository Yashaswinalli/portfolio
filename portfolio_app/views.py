from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

from .models import (SiteConfig, Skill, Project, Training,
                     Certificate, Achievement, ContactMessage)


def get_site_config():
    config, _ = SiteConfig.objects.get_or_create(id=1)
    return config


def index(request):
    config = get_site_config()
    skills_by_category = {
        'Languages': Skill.objects.filter(category='language'),
        'Frameworks': Skill.objects.filter(category='framework'),
        'Tools/Platforms': Skill.objects.filter(category='tool'),
        'Soft Skills': Skill.objects.filter(category='soft'),
    }
    projects = Project.objects.filter(featured=True).prefetch_related('bullets')
    trainings = Training.objects.all().prefetch_related('bullets')
    certificates = Certificate.objects.all()
    achievements = Achievement.objects.all()

    context = {
        'config': config,
        'skills_by_category': skills_by_category,
        'projects': projects,
        'trainings': trainings,
        'certificates': certificates,
        'achievements': achievements,
    }
    return render(request, 'portfolio_app/index.html', context)


@require_POST
def contact(request):
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()

        if not all([name, email, subject, message]):
            return JsonResponse({'success': False, 'error': 'All fields are required.'})

        # Save to database
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        # Send email
        full_message = f"""
New Portfolio Contact Message
==============================
From: {name} <{email}>
Subject: {subject}

Message:
{message}
==============================
Sent from your portfolio website.
"""
        try:
            send_mail(
                subject=f"[Portfolio] {subject} — from {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception as mail_err:
            # Still save but warn
            return JsonResponse({
                'success': True,
                'warning': 'Message saved but email delivery failed. Configure EMAIL_HOST_PASSWORD in settings.py'
            })

        return JsonResponse({'success': True, 'message': 'Message sent successfully!'})

    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
