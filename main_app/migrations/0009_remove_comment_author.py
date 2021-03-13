from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
