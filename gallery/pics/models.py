from django.db import models

# Create your models here.
class Editor(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['name']

class location(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
class Image(models.Model):
     name = models.CharField(max_length=20)
     description = models.CharField(max_length=200)
     location = models.ManyToManyField(location)
     category = models.ForeignKey(Editor)
