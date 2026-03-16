"""
Custom management command: open_admin
--------------------------------------
Opens the custom portfolio dashboard (or Django admin) in your
default web browser, optionally starting the dev server first.

Usage
-----
  python manage.py open_admin                  # opens /dashboard/ (custom)
  python manage.py open_admin --django-admin   # opens /admin/     (Django)
  python manage.py open_admin --port 8080      # use a different port
  python manage.py open_admin --runserver      # also start the dev server
"""

import webbrowser
import time
import threading
import sys

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = (
        "Open the custom portfolio admin dashboard in your default browser. "
        "Pass --django-admin to open the built-in Django admin instead."
    )

    # ── Colour helpers ────────────────────────────────────────────────────────
    CYAN   = "\033[96m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

    def add_arguments(self, parser):
        parser.add_argument(
            "--django-admin",
            action="store_true",
            default=False,
            help="Open the built-in Django /admin/ interface instead of the custom dashboard.",
        )
        parser.add_argument(
            "--port",
            type=int,
            default=8000,
            help="Port the development server is (or will be) running on. Default: 8000",
        )
        parser.add_argument(
            "--runserver",
            action="store_true",
            default=False,
            help="Also start 'runserver' before opening the browser.",
        )

    # ── Main entry ────────────────────────────────────────────────────────────
    def handle(self, *args, **options):
        port          = options["port"]
        use_django    = options["django_admin"]
        also_runserver = options["runserver"]

        path = "/admin/" if use_django else "/dashboard/"
        url  = f"http://127.0.0.1:{port}{path}"

        label = "Django Admin" if use_django else "Custom Dashboard"

        self._banner()
        self.stdout.write(
            f"{self.BOLD}{self.CYAN}  🚀  Opening {label}{self.RESET}"
        )
        self.stdout.write(
            f"{self.CYAN}  🌐  URL : {self.BOLD}{url}{self.RESET}"
        )

        if also_runserver:
            self._start_runserver_in_thread(port)
            self.stdout.write(
                f"{self.YELLOW}  ⏳  Waiting for server to boot …{self.RESET}"
            )
            time.sleep(2)

        webbrowser.open(url)

        self.stdout.write(
            f"\n{self.GREEN}  ✅  Browser opened!  "
            f"{self.RESET}If nothing appeared, navigate to:\n"
            f"      {self.BOLD}{url}{self.RESET}\n"
        )

        if also_runserver:
            self.stdout.write(
                f"{self.YELLOW}  🔄  Dev server is running — press Ctrl+C to stop.{self.RESET}\n"
            )
            # Block so the server stays alive
            try:
                threading.Event().wait()
            except KeyboardInterrupt:
                self.stdout.write(f"\n{self.RED}  🛑  Server stopped.{self.RESET}\n")
                sys.exit(0)

    # ── Helpers ───────────────────────────────────────────────────────────────
    def _banner(self):
        lines = [
            "",
            f"{self.BOLD}{self.CYAN}╔══════════════════════════════════════════╗{self.RESET}",
            f"{self.BOLD}{self.CYAN}║   Yashaswi Portfolio  —  Admin Launcher  ║{self.RESET}",
            f"{self.BOLD}{self.CYAN}╚══════════════════════════════════════════╝{self.RESET}",
            "",
        ]
        for line in lines:
            self.stdout.write(line)

    def _start_runserver_in_thread(self, port: int):
        """Launch 'runserver' on a daemon thread so it doesn't block."""
        def _run():
            call_command("runserver", f"127.0.0.1:{port}", use_reloader=False)

        t = threading.Thread(target=_run, daemon=True)
        t.start()
