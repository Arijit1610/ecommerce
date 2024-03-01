from django.contrib import admin
from .models import Fashion, Eletronices, BeautyCosmetics, BooksAndStationery, Sportsandoutdoor, HomeandKitchen
from django.utils.safestring import mark_safe


class BaseProductAdmin(admin.ModelAdmin):

    def preview_photo1(self, obj):
        if obj.photo1:
            return mark_safe('<img src="{url}" width="100px" />'.format(url=obj.photo1.url))
        else:
            return 'No Image'

    preview_photo1.short_description = 'Image Preview'


class FashionAdmin(BaseProductAdmin):
    list_display = ['fashion_name', 'fashion_section',
                    'differentfashion', 'price', 'qty', 'preview_photo1']


admin.site.register(Fashion, FashionAdmin)


class EletronicesAdmin(BaseProductAdmin):
    list_display = ['product_name', 'types', 'price', 'qty', 'preview_photo1']


admin.site.register(Eletronices, EletronicesAdmin)


class BeautyCosmeticsAdmin(BaseProductAdmin):
    list_display = ['product_name', 'types', 'price', 'qty', 'preview_photo1']


admin.site.register(BeautyCosmetics, BeautyCosmeticsAdmin)


class BooksAndStationeryAdmin(BaseProductAdmin):
    list_display = ['title', 'types', 'price', 'qty', 'preview_photo1']


admin.site.register(BooksAndStationery, BooksAndStationeryAdmin)


class SportsandoutdoorAdmin(BaseProductAdmin):
    list_display = ['product_name', 'sportscatagory',
                    'price', 'qty', 'preview_photo1']


admin.site.register(Sportsandoutdoor, SportsandoutdoorAdmin)


class HomeandKitchenAdmin(BaseProductAdmin):
    list_display = ['product_name', 'Productcatagory',
                    'price', 'qty', 'preview_photo1']


admin.site.register(HomeandKitchen, HomeandKitchenAdmin)


admin.site.site_header = "Mercury Admin Panel"
admin.site.site_title = "Mercury Admin Portal"
admin.site.index_title = "Welcome to Mercury Ecommerce"
