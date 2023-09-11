from django.shortcuts import render
from django.views import generic
from products.models import Category


# Create your views here.
# based on BoutiqueAdo walkthrough


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# class CategoryList(generic.ListView):
#     model = Category
#     queryset = Category.objects.all()
#     template_name = 'category_list.html'
