from django.contrib import admin
from .models import Author, Genre, Language, Book, BookInstance

# Register your models here.
class BookInLine(admin.TabularInline):
    model=Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines= [BookInLine]


##adds borrower field to admin
# lets you add "books" to users 
# @admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', "status", "due_back", "id")
    list_filer= ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', "borrower")        ##tells you who has taken it out
        }),
    )

class BookInstanceInLine(admin.TabularInline):
    model=BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines= [BookInstanceInLine]




admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
