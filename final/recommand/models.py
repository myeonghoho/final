from django.db import models

# Create your models here.

class upload_image(models.Model) :
    upload_image = models.FileField(upload_to = 'Uploaded Files/%y/%m/%d/', blank=True)
    컬럼_업로드날짜 = models.DateField(auto_now = True)