from django.contrib import admin

from BookCanteenPrototype.models import Book, BookUser


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'user')


class BookUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'address', 'phone', 'user')


admin.site.register(Book, BookAdmin)
admin.site.register(BookUser, BookUserAdmin)
