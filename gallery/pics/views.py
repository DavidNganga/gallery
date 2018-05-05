from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image,Category,Location,Editor

# Create your views here.
def visualize(request):
    photos = Image.get_all()
    return render (request, 'welcome.html',{"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Category.search_by_category(search_term)
        images = Image.get_Image_by_category(searched_images)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def all(request):
    img = Image.get_all()
    return render (request, 'all-stuff.html',{"img":img})
