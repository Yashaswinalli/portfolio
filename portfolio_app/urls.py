from django.urls import path
from . import views
from . import dashboard_views

urlpatterns = [
    # ── Portfolio ──
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),

    # ── Dashboard Auth ──
    path('dashboard/login/', dashboard_views.dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', dashboard_views.dashboard_logout, name='dashboard_logout'),

    # ── Dashboard Main ──
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),

    # ── Save routes ──
    path('dashboard/save/config/', dashboard_views.save_config, name='save_config'),
    path('dashboard/save/about/', dashboard_views.save_about, name='save_about'),
    path('dashboard/save/skill/', dashboard_views.save_skill, name='save_skill'),
    path('dashboard/save/project/', dashboard_views.save_project, name='save_project'),
    path('dashboard/save/training/', dashboard_views.save_training, name='save_training'),
    path('dashboard/save/cert/', dashboard_views.save_cert, name='save_cert'),
    path('dashboard/save/achievement/', dashboard_views.save_achievement, name='save_achievement'),

    # ── Get JSON routes ──
    path('dashboard/get/project/<int:pk>/', dashboard_views.get_project, name='get_project'),
    path('dashboard/get/training/<int:pk>/', dashboard_views.get_training, name='get_training'),

    # ── Delete routes ──
    path('dashboard/delete/skill/<int:pk>/', dashboard_views.delete_skill, name='delete_skill'),
    path('dashboard/delete/project/<int:pk>/', dashboard_views.delete_project, name='delete_project'),
    path('dashboard/delete/training/<int:pk>/', dashboard_views.delete_training, name='delete_training'),
    path('dashboard/delete/cert/<int:pk>/', dashboard_views.delete_cert, name='delete_cert'),
    path('dashboard/delete/achievement/<int:pk>/', dashboard_views.delete_achievement, name='delete_achievement'),
    path('dashboard/delete/message/<int:pk>/', dashboard_views.delete_message, name='delete_message'),

    # ── Message actions ──
    path('dashboard/message/read/<int:pk>/', dashboard_views.mark_message_read, name='mark_message_read'),
]
