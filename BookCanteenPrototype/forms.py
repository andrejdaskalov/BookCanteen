from django import forms
from .models import Book
from django.contrib.auth.forms import AuthenticationForm
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'description', 'image', 'new', 'subject', 'location', 'condition']
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-3 d-block'})
        self.fields['new'].widget.attrs.update({'class': 'form-check-input d-block'})

class LoginForm(AuthenticationForm):
    # override contructor
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # add class to fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-3 d-block'})
        
    
    