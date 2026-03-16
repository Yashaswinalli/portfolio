from django.db import migrations


def populate_data(apps, schema_editor):
    SiteConfig = apps.get_model('portfolio_app', 'SiteConfig')
    Skill = apps.get_model('portfolio_app', 'Skill')
    Project = apps.get_model('portfolio_app', 'Project')
    ProjectBullet = apps.get_model('portfolio_app', 'ProjectBullet')
    Training = apps.get_model('portfolio_app', 'Training')
    TrainingBullet = apps.get_model('portfolio_app', 'TrainingBullet')
    Certificate = apps.get_model('portfolio_app', 'Certificate')
    Achievement = apps.get_model('portfolio_app', 'Achievement')

    # Site Config
    SiteConfig.objects.create(
        name="Nalli Yashaswi",
        tagline="Full Stack Developer & Cybersecurity Enthusiast",
        bio="Passionate developer with expertise in cybersecurity and full-stack web development. I love building secure, scalable applications and solving complex problems with elegant solutions.",
        email="nalliyashaswi@gmail.com",
        mobile="+91-9182911785",
        github="https://github.com/Yashaswinalli",
        linkedin="https://www.linkedin.com/in/yashaswi-nalli/",
    )

    # Skills - Languages
    for i, (name, pct) in enumerate([
        ('C', 75), ('C++', 78), ('Java', 72), ('Python', 85), ('JavaScript', 88)
    ]):
        Skill.objects.create(name=name, category='language', proficiency=pct, order=i)

    # Skills - Frameworks
    for i, (name, pct) in enumerate([
        ('HTML', 90), ('CSS', 85), ('React', 82), ('Node.js', 78), ('Django', 80)
    ]):
        Skill.objects.create(name=name, category='framework', proficiency=pct, order=i)

    # Skills - Tools
    for i, (name, pct) in enumerate([
        ('Wireshark', 80), ('Nmap', 82), ('Kali Linux', 78), ('Metasploit', 75), ('Git', 85)
    ]):
        Skill.objects.create(name=name, category='tool', proficiency=pct, order=i)

    # Skills - Soft
    for i, name in enumerate([
        'Attention to Detail', 'Critical Thinking', 'Adaptability', 'Problem Solving',
        'Integrity', 'Ethics'
    ]):
        Skill.objects.create(name=name, category='soft', proficiency=85, order=i)

    # Project 1
    p1 = Project.objects.create(
        title="Zero-Trust Password Analyzer with APIs, Recommender, and Password Vault",
        description="A comprehensive password security platform with real-time threat intelligence.",
        tech_stack="JavaScript, HTML5, CSS3, REST API Integration, Data Security, Client-Side Logic",
        github_url="https://github.com/Yashaswinalli",
        start_date="Jun'25",
        end_date="Jul'25",
        featured=True, order=0
    )
    for i, text in enumerate([
        "Developed a Zero-Trust platform to analyze password entropy and enforce high-security standards.",
        "Integrated HaveBeenPwned APIs for real-time threat intelligence and breach verification.",
        "Engineered a secure Password Vault using client-side processing for localized data privacy.",
        "Designed an intelligent recommender system to enforce high-security credential standards.",
        "Built an interactive 'Password Welt' module to educate users on security best practices.",
    ]):
        ProjectBullet.objects.create(project=p1, text=text, order=i)

    # Project 2
    p2 = Project.objects.create(
        title="E-commerce Web Application",
        description="A full-featured MERN-stack e-commerce platform.",
        tech_stack="React, Node.js, MongoDB, Stripe API",
        github_url="https://github.com/Yashaswinalli",
        start_date="Nov'23",
        end_date="Dec'23",
        featured=True, order=1
    )
    for i, text in enumerate([
        "Architected a scalable MERN-stack platform for product discovery and catalog management.",
        "Implemented secure JWT authentication and role-based access to safeguard user data.",
        "Engineered a high-performance shopping cart with persistent state and real-time updates.",
        "Integrated Stripe API for secure, PCI-compliant payment processing and checkout.",
        "Optimized UX with a mobile-first, responsive interface and streamlined transaction path.",
    ]):
        ProjectBullet.objects.create(project=p2, text=text, order=i)

    # Training
    t1 = Training.objects.create(
        title="Cyber Security Training",
        organization="Lovely Professional University",
        start_date="Jun'25",
        end_date="Jul'25",
        order=0
    )
    for i, text in enumerate([
        "Executed end-to-end security assessments from reconnaissance to system exploitation.",
        "Performed network discovery and vulnerability scanning with Nmap and Nessus.",
        "Analysed real-time traffic using Wireshark to identify anomalies and data exfiltration.",
        "Simulated MITM attacks and packet sniffing using Ettercap to evaluate integrity.",
        "Conducted exploitation and post-exploitation tasks using the Metasploit Framework.",
    ]):
        TrainingBullet.objects.create(training=t1, text=text, order=i)

    # Certificates
    Certificate.objects.create(
        title="Cyber Security Essentials",
        issuer="Lovely Professional University",
        start_date="Jun'25",
        end_date="Jul'25",
        order=0
    )
    Certificate.objects.create(
        title="Ethical Hacking",
        issuer="Code Sprint",
        issuer_url="",
        start_date="Feb'24",
        end_date="Mar'24",
        order=1
    )
    Certificate.objects.create(
        title="Responsive Web Design",
        issuer="FreeCodeCamp",
        issuer_url="https://www.freecodecamp.org",
        start_date="Aug'23",
        end_date="Nov'23",
        order=2
    )

    # Achievements
    Achievement.objects.create(text="Achieved top 10% on HackerRank platform", order=0)


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data, migrations.RunPython.noop),
    ]
