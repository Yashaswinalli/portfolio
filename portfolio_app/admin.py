from django.contrib import admin
from .models import (SiteConfig, Skill, Project, ProjectBullet,
                     Training, TrainingBullet, Certificate, Achievement, ContactMessage)


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'tagline', 'bio', 'email', 'mobile')}),
        ('Social Links', {'fields': ('github', 'linkedin')}),
        ('Files', {'fields': ('resume_file', 'cv_url')}),
    )

    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class ProjectBulletInline(admin.TabularInline):
    model = ProjectBullet
    extra = 1
    fields = ('text', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'featured', 'order')
    list_editable = ('featured', 'order')
    inlines = [ProjectBulletInline]
    fieldsets = (
        ('Project Info', {'fields': ('title', 'description', 'tech_stack', 'image')}),
        ('Links', {'fields': ('github_url', 'live_url')}),
        ('Timeline', {'fields': ('start_date', 'end_date')}),
        ('Display', {'fields': ('featured', 'order')}),
    )


class TrainingBulletInline(admin.TabularInline):
    model = TrainingBullet
    extra = 1
    fields = ('text', 'order')


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start_date', 'end_date', 'order')
    list_editable = ('order',)
    inlines = [TrainingBulletInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_editable = ('proficiency', 'order')
    list_filter = ('category',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'start_date', 'end_date', 'order')
    list_editable = ('order',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('text', 'order')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at', 'is_read')
    list_filter = ('is_read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'sent_at')
    list_editable = ('is_read',)

    def has_add_permission(self, request):
        return False
