from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image,Category,Location,Editor
from django_modalview.generic.base import ModalTemplateView

# Create your views here.
def visualize(request):
    photos = Image.get_all()
    return render (request, 'welcome.html',{"photos":photos})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        print(search_term)

        images = Image.search_results(search_term)
        message = f"{search_term}"
        print(images)

        return render(request, 'search.html',{"message":message,"images": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



def all(request,image_id):

    image = Image.objects.get(id = image_id)

    return render(request,"all-stuff.html",{"image":image, id: image_id})
