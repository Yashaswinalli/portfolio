from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
import json

from .models import (SiteConfig, Skill, Project, ProjectBullet,
                     Training, TrainingBullet, Certificate, Achievement, ContactMessage)


def is_superuser(user):
    return user.is_active and user.is_superuser


def get_config():
    config, _ = SiteConfig.objects.get_or_create(id=1)
    return config


# ─── LOGIN / LOGOUT ───────────────────────────────────────────

def dashboard_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard')

    error = None
    username = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid credentials or not a superuser.'

    return render(request, 'portfolio_app/dashboard/login.html', {
        'error': error, 'username': username
    })


def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')


# ─── MAIN DASHBOARD ──────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@user_passes_test(is_superuser, login_url='/dashboard/login/')
def dashboard(request):
    config = get_config()
    skills = Skill.objects.all()
    projects = Project.objects.prefetch_related('bullets').all()
    trainings = Training.objects.prefetch_related('bullets').all()
    certificates = Certificate.objects.all()
    achievements = Achievement.objects.all()
    all_messages = ContactMessage.objects.all()
    recent_messages = all_messages[:5]

    # Group skills by category for the template
    skills_by_cat = {}
    for skill in skills:
        skills_by_cat.setdefault(skill.category, []).append(skill)

    skill_categories = [
        ('language', 'Languages'),
        ('framework', 'Frameworks'),
        ('tool', 'Tools/Platforms'),
        ('soft', 'Soft Skills'),
    ]

    return render(request, 'portfolio_app/dashboard/dashboard.html', {
        'config': config,
        'skills_by_cat': skills_by_cat,
        'skill_categories': skill_categories,
        'projects': projects,
        'trainings': trainings,
        'certificates': certificates,
        'achievements': achievements,
        'all_messages': all_messages,
        'recent_messages': recent_messages,
        'skills_count': skills.count(),
        'projects_count': projects.count(),
        'certs_count': certificates.count(),
        'messages_count': all_messages.count(),
        'unread_count': all_messages.filter(is_read=False).count(),
    })


# ─── SAVE CONFIG ─────────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@user_passes_test(is_superuser, login_url='/dashboard/login/')
def save_config(request):
    if request.method == 'POST':
        config = get_config()
        config.name = request.POST.get('name', config.name).strip()
        config.tagline = request.POST.get('tagline', config.tagline).strip()
        config.bio = request.POST.get('bio', config.bio).strip()
        config.email = request.POST.get('email', config.email).strip()
        config.mobile = request.POST.get('mobile', config.mobile).strip()
        config.github = request.POST.get('github', config.github).strip()
        config.linkedin = request.POST.get('linkedin', config.linkedin).strip()
        config.cv_url = request.POST.get('cv_url', '').strip()
        if 'resume_file' in request.FILES:
            config.resume_file = request.FILES['resume_file']
        config.save()
    return redirect('/dashboard/?saved=1&panel=config')


# ─── SAVE ABOUT ──────────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@user_passes_test(is_superuser, login_url='/dashboard/login/')
def save_about(request):
    if request.method == 'POST':
        config = get_config()
        config.education_text = request.POST.get('education_text', config.education_text).strip()
        config.tags = request.POST.get('tags', config.tags).strip()
        config.stat1_value = request.POST.get('stat1_value', '').strip()
        config.stat1_label = request.POST.get('stat1_label', '').strip()
        config.stat2_value = request.POST.get('stat2_value', '').strip()
        config.stat2_label = request.POST.get('stat2_label', '').strip()
        config.stat3_value = request.POST.get('stat3_value', '').strip()
        config.stat3_label = request.POST.get('stat3_label', '').strip()
        config.stat4_value = request.POST.get('stat4_value', '').strip()
        config.stat4_label = request.POST.get('stat4_label', '').strip()
        config.save()
    return redirect('/dashboard/?saved=1&panel=about')


# ─── SAVE SKILL ──────────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@user_passes_test(is_superuser, login_url='/dashboard/login/')
def save_skill(request):
    if request.method == 'POST':
        skill_id = request.POST.get('skill_id', '').strip()
        name = request.POST.get('name', '').strip()
        category = request.POST.get('category', 'language')
        proficiency = int(request.POST.get('proficiency', 80))
        order = int(request.POST.get('order', 0))

        if skill_id:
            skill = get_object_or_404(Skill, id=skill_id)
        else:
            skill = Skill()

        skill.name = name
        skill.category = category
        skill.proficiency = proficiency
        skill.order = order
        skill.save()
    return redirect('/dashboard/?saved=1&panel=skills')


# ─── DELETE SKILL ────────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@require_POST
def delete_skill(request, pk):
    obj = get_object_or_404(Skill, pk=pk)
    obj.delete()
    return JsonResponse({'success': True})


# ─── SAVE PROJECT ────────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@user_passes_test(is_superuser, login_url='/dashboard/login/')
def save_project(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id', '').strip()
        if project_id:
            project = get_object_or_404(Project, id=project_id)
        else:
            project = Project()

        project.title = request.POST.get('title', '').strip()
        project.description = request.POST.get('description', '').strip()
        project.tech_stack = request.POST.get('tech_stack', '').strip()
        project.github_url = request.POST.get('github_url', '').strip()
        project.live_url = request.POST.get('live_url', '').strip()
        project.start_date = request.POST.get('start_date', '').strip()
        project.end_date = request.POST.get('end_date', '').strip()
        project.order = int(request.POST.get('order', 0))
        project.featured = True
        project.save()

        # Replace bullets
        project.bullets.all().delete()
        bullets = request.POST.getlist('project-bullet[]')
        for i, text in enumerate(bullets):
            text = text.strip()
            if text:
                ProjectBullet.objects.create(project=project, text=text, order=i)

    return redirect('/dashboard/?saved=1&panel=projects')


# ─── GET PROJECT JSON ─────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
def get_project(request, pk):
    p = get_object_or_404(Project, pk=pk)
    return JsonResponse({
        'title': p.title, 'description': p.description,
        'tech_stack': p.tech_stack, 'github_url': p.github_url,
        'live_url': p.live_url, 'start_date': p.start_date,
        'end_date': p.end_date, 'order': p.order,
        'bullets': list(p.bullets.values_list('text', flat=True)),
    })


# ─── DELETE PROJECT ───────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@require_POST
def delete_project(request, pk):
    get_object_or_404(Project, pk=pk).delete()
    return JsonResponse({'success': True})


# ─── SAVE TRAINING ────────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@user_passes_test(is_superuser, login_url='/dashboard/login/')
def save_training(request):
    if request.method == 'POST':
        training_id = request.POST.get('training_id', '').strip()
        if training_id:
            training = get_object_or_404(Training, id=training_id)
        else:
            training = Training()

        training.title = request.POST.get('title', '').strip()
        training.organization = request.POST.get('organization', '').strip()
        training.start_date = request.POST.get('start_date', '').strip()
        training.end_date = request.POST.get('end_date', '').strip()
        training.order = int(request.POST.get('order', 0))
        training.save()

        training.bullets.all().delete()
        bullets = request.POST.getlist('training-bullet[]')
        for i, text in enumerate(bullets):
            text = text.strip()
            if text:
                TrainingBullet.objects.create(training=training, text=text, order=i)

    return redirect('/dashboard/?saved=1&panel=training')


# ─── GET TRAINING JSON ────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
def get_training(request, pk):
    t = get_object_or_404(Training, pk=pk)
    return JsonResponse({
        'title': t.title, 'organization': t.organization,
        'start_date': t.start_date, 'end_date': t.end_date, 'order': t.order,
        'bullets': list(t.bullets.values_list('text', flat=True)),
    })


# ─── DELETE TRAINING ──────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@require_POST
def delete_training(request, pk):
    get_object_or_404(Training, pk=pk).delete()
    return JsonResponse({'success': True})


# ─── SAVE CERT ────────────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@user_passes_test(is_superuser, login_url='/dashboard/login/')
def save_cert(request):
    if request.method == 'POST':
        cert_id = request.POST.get('cert_id', '').strip()
        if cert_id:
            cert = get_object_or_404(Certificate, id=cert_id)
        else:
            cert = Certificate()

        cert.title = request.POST.get('title', '').strip()
        cert.issuer = request.POST.get('issuer', '').strip()
        cert.issuer_url = request.POST.get('issuer_url', '').strip()
        cert.start_date = request.POST.get('start_date', '').strip()
        cert.end_date = request.POST.get('end_date', '').strip()
        cert.order = int(request.POST.get('order', 0))
        cert.save()

    return redirect('/dashboard/?saved=1&panel=certs')


# ─── DELETE CERT ──────────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@require_POST
def delete_cert(request, pk):
    get_object_or_404(Certificate, pk=pk).delete()
    return JsonResponse({'success': True})


# ─── SAVE ACHIEVEMENT ─────────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@user_passes_test(is_superuser, login_url='/dashboard/login/')
def save_achievement(request):
    if request.method == 'POST':
        ach_id = request.POST.get('achievement_id', '').strip()
        if ach_id:
            ach = get_object_or_404(Achievement, id=ach_id)
        else:
            ach = Achievement()
        ach.text = request.POST.get('text', '').strip()
        ach.order = int(request.POST.get('order', 0))
        ach.save()

    return redirect('/dashboard/?saved=1&panel=achievements')


# ─── DELETE ACHIEVEMENT ───────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@require_POST
def delete_achievement(request, pk):
    get_object_or_404(Achievement, pk=pk).delete()
    return JsonResponse({'success': True})


# ─── MESSAGE READ / DELETE ────────────────────────────────────

@login_required(login_url='/dashboard/login/')
@require_POST
def mark_message_read(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.is_read = True
    msg.save()
    return JsonResponse({'success': True})


@login_required(login_url='/dashboard/login/')
@require_POST
def delete_message(request, pk):
    get_object_or_404(ContactMessage, pk=pk).delete()
    return JsonResponse({'success': True})
