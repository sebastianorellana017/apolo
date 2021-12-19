from miapp.models import *

def  get_categories(request):
    
    categories_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=categories_use).values_list('id','name')

    return {
        'categories': categories,
        'id': categories_use
    }