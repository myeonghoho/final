from django.db import models

# Create your models here.

class Upload_image(models.Model) :
    title = models.CharField("제목", max_length = 100, blank = True)
    upload_image = models.ImageField("이미지", upload_to = "media/images/", blank = True)

    def __str__(self):
        return self.title