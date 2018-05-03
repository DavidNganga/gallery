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
