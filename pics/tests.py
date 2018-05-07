from django.test import TestCase
from .models import Editor,Image,location


# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.david= Editor(name = 'David')

    def test_instance(self):
        self.assertTrue(isinstance(self.david,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.david.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.david= Editor(name = 'David')
        self.david.save_editor()

        # Creating a new tag and saving it
        self.new_location = location(name = 'testing')
        self.new_location.save()

        self.new_image= Image(name = 'joker',description= 'hahaha',category = self.comics)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        location.objects.all().delete()
        Image.objects.all().delete()
