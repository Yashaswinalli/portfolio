from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import AdminSite
from portfolio_app.models import Skill, Project, Training, Certificate, ContactMessage


class PortfolioAdminSite(AdminSite):
    site_header = "Nalli Yashaswi — Portfolio Admin"
    site_title = "Portfolio Admin"
    index_title = "Dashboard"

    def each_context(self, request):
        context = super().each_context(request)
        context['quick_stats'] = [
            {'icon': '🛠', 'label': 'Skills',    'count': Skill.objects.count()},
            {'icon': '🚀', 'label': 'Projects',  'count': Project.objects.count()},
            {'icon': '📚', 'label': 'Trainings', 'count': Training.objects.count()},
            {'icon': '🎓', 'label': 'Certs',     'count': Certificate.objects.count()},
            {'icon': '✉',  'label': 'Messages',  'count': ContactMessage.objects.filter(is_read=False).count()},
        ]
        return context


# Replace default admin site
admin.site.__class__ = PortfolioAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
