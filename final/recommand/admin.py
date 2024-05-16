from django.contrib import admin
from recommand.models import Upload_image

# Register your models here.
@admin.register(Upload_image)
class Upload_imageAdmin(admin.ModelAdmin):
    list_display = ["title", "upload_image"]