# Generated by Django 5.1.3 on 2024-12-07 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_alter_library_options_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'permissions': [('can_add_books', 'Can add books'), ('can_remove_books', 'Can remove books'), ('can_change_book', 'Can change book'), ('can_delete_book', 'Can delete book')]},
        ),
    ]
