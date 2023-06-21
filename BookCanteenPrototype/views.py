from django.shortcuts import render, redirect

from BookCanteenPrototype.models import Book

from django.db.models import Q

# Create your views here.

# index view
def index(request):
    return render(request, 'index.html')



def results(request):
    query = request.GET['query'] 
    new = request.GET.get('new', '0')
    is_new = True if new == '1' else False

    if query and query != '':
        results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(subject__icontains=query),  new=is_new)
    else:
        results = Book.objects.filter(new=is_new)
    return render(request, 'results.html', {'results': results, 'query': query, 'new': is_new})
  