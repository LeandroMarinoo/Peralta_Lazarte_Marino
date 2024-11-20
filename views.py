from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
def index_page(request):
    return render(request, 'index.html')

def getAllImagesAndFavouriteList(search_msg, request):
    images = services.getAllImages(search_msg)
    favourite_list = services.getAllFavourites(request)

    return images, favourite_list




def home(request):
    images = services.getAllImages()
    favourite_list = []
    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
def search(request):
    search_msg = request.POST.get('query', '')
    if search_msg == "":
        search_msg = None
    images, favourite_list = getAllImagesAndFavouriteList(search_msg, request)
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})
@login_required
def getAllFavouritesByUser(request):
    favourite_list = services.getAllFavouritesByUser(request)
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })
@login_required
def saveFavourite(request):
    services.saveFavourite(request)
    return redirect("/buscar")
@login_required
def deleteFavourite(request):
    services.deleteFavourite
    return redirect("/favourites")
@login_required
def exit(request):
    logout(request)
    return redirect('/')