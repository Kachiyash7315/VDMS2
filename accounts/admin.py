from asyncio import format_helpers
from django.contrib import admin
from django.utils.html import format_html
from .models import Profile,Service,Category

# Register your models here.


admin.site.register(Profile)

admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('Name','Category','Price','Tags','Description','Edit','Delete')

    def Edit(self , obj):
        return format_html(f'<a href="/admin/api/service/{obj.id}/change/" class="btn btn-sm btn-outline-info btn-flat changelink">Change</a>')
    
    def Delete(self , obj):
        return format_html(f'<a href="/admin/api/service/{obj.id}/delete/" class="btn btn-outline-danger form-control">Delete</a>')

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name','Image','Edit','Delete')

    def Edit(self , obj):
        return format_html(f'<a href="/admin/api/category/{obj.id}/change/" class="btn btn-sm btn-outline-info btn-flat changelink">Change</a>')
    
    def Delete(self , obj):
        return format_html(f'<a href="/admin/api/category/{obj.id}/delete/" class="btn btn-outline-danger form-control">Delete</a>')




