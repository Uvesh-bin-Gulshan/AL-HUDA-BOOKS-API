from django.contrib import admin
from .models import Book, Translation, ContentSection

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'uploaded_at')
    search_fields = ('title', 'author')
    list_filter = ('uploaded_at',)

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('book', 'language', 'translator', 'is_original', 'publication_date')
    list_filter = ('language', 'is_original', 'publication_date')
    search_fields = ('book__title', 'translator', 'language')
    list_select_related = ('book',)

@admin.register(ContentSection)
class ContentSectionAdmin(admin.ModelAdmin):
    list_display = ('translation', 'index', 'sub_index', 'page_number')
    list_filter = ('translation__book',)
    search_fields = ('translation__book__title', 'index', 'sub_index', 'content')
    list_select_related = ('translation',)

