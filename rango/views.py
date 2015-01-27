from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category,Page

# Create your views here.
def index(request):
	Category_list=Category.objects.order_by('-likes')[:5]
	context={'boldmessage': "I am bold", 'categories': Category_list}
	return render(request, 'rango/index.html', context)
	# return HttpResponse("Welcome to the world of rango. Rango says hello world!<br> Learn more <a href='/rango/about'>here</a>")

def about(request):
	# return HttpResponse("This is the about page<br><a href='/rango'>Go back</a>")
	context={}
	return render(request, 'rango/about.html', context)

# def category(request, slug_name):
# 	# context={}
# 	try:
# 		category=Category.objects.get(slug=slug_name)
# 		# context['category_name']= category.name
# 		pages=Page.objects.filter(category=category)
# 		# context['pages'] = pages
#         # context['category'] = category
#         context={'category_name':category.name, 'category':category, 'pages':pages}
#     except Category.DoesNotExist:
#     	pass
#     return render(request, 'rango/category.html', context)
def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)