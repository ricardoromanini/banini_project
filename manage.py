import os
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banini_project.settings')
execute_from_command_line(__import__('sys').argv)