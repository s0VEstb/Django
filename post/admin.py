from django.contrib import admin

from post.models import Product, Category, Review, Catalog

class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'catalog')
    list_display_links = ('name',)
    list_editable = ('price', 'category')
    list_filter = ('created_at', 'price', 'category')
    search_fields = ('name', 'category')
    readonly_fields = ('created_at', 'updated_at', 'id')
    fields = ('id', 'image', 'name', 'price', 'category', 'catalog', 'created_at', 'updated_at')
    inlines = [ReviewInline]

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Catalog)
