from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Book, Translation, ContentSection

# BookAdmin with Import/Export functionality
# TranslationAdmin with Import/Export functionality
@admin.register(Translation)
class TranslationAdmin(ImportExportModelAdmin):
    list_display = ('book', 'language', 'translator', 'is_original', 'publication_date')
    list_filter = ('language', 'is_original', 'publication_date')
    search_fields = ('book__title', 'translator', 'language')
    list_select_related = ('book',)

# ContentSectionAdmin with Import/Export functionality
@admin.register(ContentSection)
class ContentSectionAdmin(ImportExportModelAdmin):
    list_display = ('translation', 'index', 'sub_index', 'page_number')
    list_filter = ('translation__book',)
    search_fields = ('translation__book__title', 'index', 'sub_index', 'content')
    list_select_related = ('translation',)

from import_export import resources
from .models import Book

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'uploaded_at')  # Specify fields to include
        export_order = ('id', 'title', 'author', 'uploaded_at')  # Specify export order
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_display = ('title', 'author', 'uploaded_at')
    search_fields = ('title', 'author')
    list_filter = ('uploaded_at',)
