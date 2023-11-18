from django.db import models

class Facts(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(max_length=99999999,null=True,blank=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=99999999, null=True, blank=True)
    languages = models.CharField(max_length=99999999, null=True, blank=True)
    frameworks = models.CharField(max_length=99999999, null=True, blank=True)
    image_url = models.CharField(max_length=99999999, null=True, blank=True)


    def __str__(self):
        return self.title


class Info(models.Model):
    about = models.TextField(max_length=99999999, null=True, blank=True)
# Create your models here.
