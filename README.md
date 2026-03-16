# 🚀 Nalli Yashaswi — 3D Animated Portfolio

A stunning, professional Django portfolio with:
- ✨ 3D animated cube & particle background
- 🌙 Dark / Light mode toggle
- 💻 Interactive terminal (Ctrl+` to open)
- 📧 Functional contact form (emails you directly)
- 🛠 Full admin interface (customize everything via GUI)
- 📱 Fully responsive design

---

## ⚡ Quick Start

### 1. Install dependencies
```bash
pip install django Pillow
```

### 2. Run setup (creates DB + superuser)
```bash
python setup.py
```

### 3. Start the server
```bash
python manage.py runserver
```

### 4. Visit your portfolio
- **Portfolio**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Login**: `admin` / `admin123`

---

## 📧 Enable Contact Form Emails

1. Go to your Google Account → Security → App Passwords
2. Create an App Password for "Mail"
3. Open `portfolio_project/settings.py`
4. Set `EMAIL_HOST_PASSWORD = 'your-16-char-app-password'`

---

## 🛠 Admin Panel Features

Login at `/admin/` with your superuser credentials.

| Section | What you can edit |
|---------|-------------------|
| **Site Configuration** | Name, bio, email, social links, resume upload |
| **Skills** | Add/edit/delete skills with proficiency % |
| **Projects** | Full project management with bullet points |
| **Training** | Training/internship history with details |
| **Certificates** | Certifications with issuer links |
| **Achievements** | Notable achievements |
| **Contact Messages** | View all messages sent through the form |

---

## 💻 Terminal Commands

Open with: **Ctrl + `** or click **$ terminal** in navbar

| Command | Description |
|---------|-------------|
| `help` | Show all commands |
| `about` | Personal info |
| `skills` | Tech stack |
| `projects` | Project list |
| `certs` | Certificates |
| `education` | Academic background |
| `achievements` | Achievements |
| `goto <section>` | Navigate to section |
| `theme` | Toggle dark/light |
| `clear` | Clear terminal |
| `exit` | Close terminal |

---

## 📁 Project Structure

```
portfolio/
├── manage.py
├── setup.py              ← Run this first!
├── requirements.txt
├── portfolio_project/
│   ├── settings.py       ← Configure email here
│   └── urls.py
└── portfolio_app/
    ├── models.py          ← Data models
    ├── views.py           ← Contact form logic
    ├── admin.py           ← Admin customization
    ├── migrations/        ← DB migrations (pre-filled with your CV data)
    └── templates/
        └── portfolio_app/
            └── index.html ← Main portfolio template
```

---

## 🎨 Customization

All content is editable via **Admin Panel** at `/admin/`.

For styling changes, edit the `<style>` block in `index.html`.

Key CSS variables (in `:root`):
- `--accent`: Primary color (default: `#00f5c4` cyan-green)
- `--accent2`: Secondary color (default: `#7c3aed` purple)
- `--font-display`: Display font (default: Syne)
- `--font-mono`: Monospace font (default: Space Mono)

---

Built with ❤️ · Django 4.2+ · Python 3.10+
