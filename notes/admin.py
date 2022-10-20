from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from .models import *


class NotesAdmin(admin.ModelAdmin):
    model = Notes
    list_display = ['user', 'uploadingdate', 'branch', 'subject', 'notesfile', 'filetype', 'status']
    list_filter = ['branch', 'subject', 'status']


# Register your models here.
admin.site.register(Signup)
admin.site.register(Notes, NotesAdmin)
