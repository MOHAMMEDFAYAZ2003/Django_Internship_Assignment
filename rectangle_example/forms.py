from django import forms
from .models import Rectangle

class RectangleForm(forms.ModelForm):
    class Meta:
        model = Rectangle
        fields = ["width", "height"]  # Ensure these match the model
