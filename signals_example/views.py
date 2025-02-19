from django.shortcuts import render

def test_signals(request):
    from .models import MyModel  
    obj = MyModel.objects.create(name="Test Object")
    return render(request, "test.html", {"object": obj})
