#!/usr/bin/env python
"""
Quick setup script for Yashaswi's Portfolio
Run this once after installing Django:
    python setup.py
"""
import os
import sys
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
    
    print("\n🚀 Yashaswi Portfolio Setup\n" + "="*40)
    
    try:
        django.setup()
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        print("Make sure Django is installed: pip install django Pillow")
        sys.exit(1)
    
    from django.core.management import call_command
    
    print("\n📦 Running migrations...")
    call_command('migrate', '--run-syncdb', verbosity=1)
    
    print("\n👤 Creating superuser...")
    print("   Username: admin")
    print("   Password: admin123")
    print("   (Change this after first login!)\n")
    
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'nalliyashaswi@gmail.com', 'admin123')
        print("   ✓ Superuser created: admin / admin123")
    else:
        print("   ⚠ Admin user already exists.")
    
    print("\n" + "="*40)
    print("✅ Setup complete!\n")
    print("Start the server:")
    print("   python manage.py runserver\n")
    print("Then visit:")
    print("   Portfolio : http://127.0.0.1:8000/")
    print("   Admin     : http://127.0.0.1:8000/admin/")
    print("   Login     : admin / admin123")
    print("\n⚠  IMPORTANT: Configure email in portfolio_project/settings.py")
    print("   Set EMAIL_HOST_PASSWORD to your Gmail App Password")
    print("="*40 + "\n")


if __name__ == '__main__':
    main()
