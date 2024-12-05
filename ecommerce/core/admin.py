from django.contrib import admin
from . import models

# Register individual models
admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Blog)
admin.site.register(models.HeoroSlider)

# Inline for NewArival
class NewArivalImageInline(admin.TabularInline):
    model = models.NewArivalImage
    extra = 1  # Number of extra forms in the inline

@admin.register(models.NewArival)
class NewArivalAdmin(admin.ModelAdmin):
    inlines = [NewArivalImageInline]
    list_display = ('name', 'price', 'category', 'stock_out', 'sales_price')

# Inline for BestSales
class BestSalesImageInline(admin.TabularInline):
    model = models.BestSalesImage
    extra = 1

@admin.register(models.BestSales)
class BestSalesAdmin(admin.ModelAdmin):
    inlines = [BestSalesImageInline]
    list_display = ('name', 'price', 'category', 'stock_out', 'sales_price')

# Admin for FirstBanner
@admin.register(models.FirstBanner)
class FirstBannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_out', 'sales_price')


# Admin for FirstBanner
@admin.register(models.SecondBanner)
class SecondBannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_out', 'sales_price')

@admin.register(models.ThirdBanner)
class ThirdBannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_out', 'sales_price')

# # Inline for SecondBanner
# class SecondBannerImageInline(admin.TabularInline):
#     model = models.SecondBannerImage
#     max_num = 4  # Limit to 4 images

# @admin.register(models.SecondBanner)
# class SecondBannerAdmin(admin.ModelAdmin):
#     inlines = [SecondBannerImageInline]
#     list_display = ('name', 'price', 'category', 'stock_out', 'sales_price')

# Inline for ThirdBanner
# class ThirdBannerImageInline(admin.TabularInline):
#     model = models.ThirdBannerImage
#     max_num = 4  # Limit to 4 images

# @admin.register(models.ThirdBanner)
# class ThirdBannerAdmin(admin.ModelAdmin):
#     inlines = [ThirdBannerImageInline]
#     list_display = ('name', 'price', 'category', 'stock_out', 'sales_price')
