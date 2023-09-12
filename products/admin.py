from django.contrib import admin
from .models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'product', 'created_on')
    Search_fields = ('name', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
