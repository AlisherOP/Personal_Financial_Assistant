from django import forms
from django.core.validators import FileExtensionValidator
from .models import Expense


class ExpenseForm(forms.ModelForm):
    receipt_image = forms.ImageField(
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp', 'avif'])]
    )

    class Meta:
        model = Expense
        fields = ['receipt_image']
