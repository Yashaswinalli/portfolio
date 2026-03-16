from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_populate_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='cv_url',
            field=models.URLField(blank=True, help_text='Public link to your CV (Google Drive, Notion, etc.)'),
        ),
    ]
