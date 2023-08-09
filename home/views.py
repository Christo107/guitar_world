from django.shortcuts import render

# Create your views here.
# based on BoutiqueAdo walkthrough


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
