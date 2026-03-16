@echo off
:: ─────────────────────────────────────────────────────────────
::  admin  —  Yashaswi Portfolio Admin Launcher
::
::  Usage:
::    admin                   Open custom dashboard  (/dashboard/)
::    admin --django-admin    Open Django admin       (/admin/)
::    admin --runserver       Start server then open  (/dashboard/)
::    admin --port 8080       Use a custom port
::    admin --help            Show all options
:: ─────────────────────────────────────────────────────────────

python manage.py open_admin %*
