from django.db import models


class SiteConfig(models.Model):
    name = models.CharField(max_length=100, default="Nalli Yashaswi")
    tagline = models.CharField(max_length=200, default="Full Stack Developer & Cybersecurity Enthusiast")
    bio = models.TextField(default="Passionate developer building secure, scalable web applications.")
    email = models.EmailField(default="nalliyashaswi@gmail.com")
    mobile = models.CharField(max_length=20, default="+91-9182911785")
    github = models.URLField(default="https://github.com/Yashaswinalli")
    linkedin = models.URLField(default="https://www.linkedin.com/in/yashaswi-nalli/")
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    cv_url = models.URLField(blank=True, help_text="Public link to your CV (Google Drive, Notion, etc.)")

    # ── About Section Fields ──
    education_text = models.TextField(
        default="Currently pursuing <strong>B.Tech in Computer Science & Engineering</strong> at <strong>Lovely Professional University</strong>, Phagwara, Punjab with a CGPA of <strong>6.5</strong>. Passionate about cybersecurity, ethical hacking, and building secure full-stack applications.",
        help_text="HTML allowed. Displayed below bio in the About section."
    )
    tags = models.CharField(
        max_length=500,
        default="JavaScript,Python,C++,Cybersecurity,MERN Stack,Django,Kali Linux",
        help_text="Comma-separated tags shown as floating badges in the About section."
    )
    stat1_value = models.CharField(max_length=30, default="6.5", blank=True)
    stat1_label = models.CharField(max_length=50, default="CGPA", blank=True)
    stat2_value = models.CharField(max_length=30, default="Top 10%", blank=True)
    stat2_label = models.CharField(max_length=50, default="HackerRank", blank=True)
    stat3_value = models.CharField(max_length=30, default="3+", blank=True)
    stat3_label = models.CharField(max_length=50, default="Certificates", blank=True)
    stat4_value = models.CharField(max_length=30, default="2+", blank=True)
    stat4_label = models.CharField(max_length=50, default="Projects", blank=True)

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return f"Config: {self.name}"

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def get_stats(self):
        stats = []
        for i in range(1, 5):
            val = getattr(self, f'stat{i}_value', '')
            label = getattr(self, f'stat{i}_label', '')
            if val and label:
                stats.append({'value': val, 'label': label})
        return stats


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Languages'),
        ('framework', 'Frameworks'),
        ('tool', 'Tools/Platforms'),
        ('soft', 'Soft Skills'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80, help_text="Percentage 0-100")
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class or emoji")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated technologies")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    start_date = models.CharField(max_length=50, blank=True)
    end_date = models.CharField(max_length=50, blank=True)
    featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]


class ProjectBullet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bullets')
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} — bullet {self.order}"


class Training(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.title} @ {self.organization}"


class TrainingBullet(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='bullets')
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.training.title} — bullet {self.order}"


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issuer_url = models.URLField(blank=True)
    start_date = models.CharField(max_length=50, blank=True)
    end_date = models.CharField(max_length=50, blank=True)
    credential_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.title} — {self.issuer}"


class Achievement(models.Model):
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text[:60]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"From {self.name} — {self.subject}"
