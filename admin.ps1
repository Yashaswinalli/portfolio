# ─────────────────────────────────────────────────────────────
#  admin.ps1  —  Yashaswi Portfolio Admin Launcher (PowerShell)
#
#  Usage:
#    .\admin.ps1                   Open custom dashboard  (/dashboard/)
#    .\admin.ps1 --django-admin    Open Django admin       (/admin/)
#    .\admin.ps1 --runserver       Start server then open  (/dashboard/)
#    .\admin.ps1 --port 8080       Use a custom port
#    .\admin.ps1 --help            Show all options
# ─────────────────────────────────────────────────────────────

python manage.py open_admin @args
