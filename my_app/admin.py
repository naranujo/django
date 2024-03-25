from django.contrib import admin

# Register your models here.
from .models import *

class selfcare_blogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    list_filter = ("title",)

admin.site.register(Category)
admin.site.register(Post, selfcare_blogAdmin)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Avatar)