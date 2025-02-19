from django.shortcuts import render, get_object_or_404, redirect
from .models import Rectangle
from .forms import RectangleForm

# List all rectangles
def rectangle_list(request):
    rectangles = Rectangle.objects.all()
    return render(request, "rectangle_example/rectangle_list.html", {"rectangles": rectangles})

# Create a new rectangle
def create_rectangle(request):
    if request.method == "POST":
        form = RectangleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rectangle_list")  
    else:
        form = RectangleForm()
    return render(request, "rectangle_example/create_rectangle.html", {"form": form})
