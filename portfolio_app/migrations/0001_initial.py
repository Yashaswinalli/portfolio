from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('issuer', models.CharField(max_length=200)),
                ('issuer_url', models.URLField(blank=True)),
                ('start_date', models.CharField(blank=True, max_length=50)),
                ('end_date', models.CharField(blank=True, max_length=50)),
                ('credential_url', models.URLField(blank=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order', '-id']},
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-sent_at']},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tech_stack', models.CharField(help_text='Comma-separated technologies', max_length=300)),
                ('github_url', models.URLField(blank=True)),
                ('live_url', models.URLField(blank=True)),
                ('start_date', models.CharField(blank=True, max_length=50)),
                ('end_date', models.CharField(blank=True, max_length=50)),
                ('featured', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
            ],
            options={'ordering': ['order', '-id']},
        ),
        migrations.CreateModel(
            name='ProjectBullet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bullets', to='portfolio_app.project')),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Nalli Yashaswi', max_length=100)),
                ('tagline', models.CharField(default='Full Stack Developer & Cybersecurity Enthusiast', max_length=200)),
                ('bio', models.TextField(default='Passionate developer building secure, scalable web applications.')),
                ('email', models.EmailField(default='nalliyashaswi@gmail.com', max_length=254)),
                ('mobile', models.CharField(default='+91-9182911785', max_length=20)),
                ('github', models.URLField(default='https://github.com/Yashaswinalli')),
                ('linkedin', models.URLField(default='https://www.linkedin.com/in/yashaswi-nalli/')),
                ('resume_file', models.FileField(blank=True, null=True, upload_to='resume/')),
            ],
            options={'verbose_name': 'Site Configuration', 'verbose_name_plural': 'Site Configuration'},
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('language', 'Languages'), ('framework', 'Frameworks'), ('tool', 'Tools/Platforms'), ('soft', 'Soft Skills')], max_length=20)),
                ('proficiency', models.IntegerField(default=80, help_text='Percentage 0-100')),
                ('icon', models.CharField(blank=True, help_text='Icon class or emoji', max_length=50)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order', 'name']},
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['order', '-id']},
        ),
        migrations.CreateModel(
            name='TrainingBullet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bullets', to='portfolio_app.training')),
            ],
            options={'ordering': ['order']},
        ),
    ]
