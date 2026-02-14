from django.contrib import admin
from .models import Expense
from django.utils.html import format_html

# admin.site.register(Expense)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    # What you see in the main list
    list_display = ('thumbnail', 'merchant', 'amount', 'user', 'date')

    # Allows you to click the merchant or amount to edit
    list_editable = ('merchant', 'amount')

    # Adds a sidebar filter on the right
    list_filter = ('date', 'user')

    # Search functionality
    search_fields = ('merchant', 'amount')

    # This function creates the thumbnail preview
    def thumbnail(self, obj):
        if obj.receipt_image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 5px;" />', obj.receipt_image.url)
        return "No Image"

    thumbnail.short_description = 'Receipt Preview'
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)
