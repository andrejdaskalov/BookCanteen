from django.shortcuts import render, redirect

from BookCanteenPrototype.models import Book


# Create your views here.

# index view
def index(request):
    return render(request, 'index.html')


def results(request):
    query = request.GET['query']
    new = request.GET['new']
    is_new = True if new == '1' else False

    results = Book.objects.filter(title__icontains=query, new=is_new)
    return render(request, 'results.html', {'results': results, 'query': query, 'new': new})
  