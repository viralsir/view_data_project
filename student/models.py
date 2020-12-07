from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=50)
    maths=models.IntegerField()
    sci=models.IntegerField()
    eng=models.IntegerField()

    def __str__(self):
        return f"Student- {self.sname}";
