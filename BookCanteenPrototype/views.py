from django.shortcuts import render, redirect

from BookCanteenPrototype.models import Book, BookUser

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
        results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query), new=is_new) #also subject once i add it
    else:
        results = Book.objects.filter(new=is_new)

    user = request.user
    bookkuser = BookUser.objects.get(user=user)
    return render(request, 'results.html', {'results': results, 'query': query, 'new': is_new, 'bookuser': bookkuser})

def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user
    bookkuser = BookUser.objects.get(user=user)

    query = request.GET['query'] 
    new = request.GET.get('new', '0')
    return render(request, 'details.html', {'book': book, 'bookuser': bookkuser, "query": query, "new": new})
  