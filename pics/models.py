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

class Location(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name


class Image(models.Model):
     name = models.CharField(max_length=20)
     image_url = models.TextField(blank = True)
     description = models.CharField(max_length=200)
     location = models.ForeignKey(Location, null=True)
     category = models.ForeignKey(Category,null=True)
     Image_image = models.ImageField(upload_to = 'images/',null = True)

     @classmethod
     def get_all(cls):
         pics = cls.objects.all()
         return pics


     def get_Image_by_id(cls,id):
        images = cls.objects.get(id=id)
        return images

     @classmethod
     def search_results(cls,search_term):
         pics = cls.objects.filter(category__name__icontains=search_term)
         print(pics)
         return pics
