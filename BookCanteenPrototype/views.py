from django.shortcuts import render, redirect
from BookCanteenPrototype.forms import BookForm, LoginForm

from BookCanteenPrototype.models import Book, BookUser

from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

# index view
def index(request):
    return render(request, 'index.html')


@login_required
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

@login_required
def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user
    bookkuser = BookUser.objects.get(user=user)

    query = request.GET['query'] 
    new = request.GET.get('new', '0')
    return render(request, 'details.html', {'book': book, 'bookuser': bookkuser, "query": query, "new": new})

@login_required
def buy_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user
    bookuser = BookUser.objects.get(user=user)
    # book.delete()
    return render(request, 'buy_page.html', {'book': book, 'bookuser': bookuser})

@login_required
def thank_you(request):
    return render(request, 'thankyou.html', {'title': 'Thank you! The seller will contact you shortly.', 'message': 'In the meantime, you can check out other books!'})

@login_required
def thank_you_seller(request):
    return render(request, 'thankyou.html', {'title': 'Thank you!', 'message': 'We are reviewing your submission and we will get back to you once it’s live.'})

@login_required
def sell(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('thank_you_seller')
        else:
            print(form.errors)
    return render(request, 'sell.html' , {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})