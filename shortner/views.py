from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

def home(request):
    short_url = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            obj = form.save()
            short_url = request.build_absolute_uri('/') + obj.short_code
    else:
        form = URLForm()
    return render(request, 'shortner/home.html', {'form': form, 'short_url': short_url})

def redirect_url(request, short_code):
    obj = get_object_or_404(URL, short_code=short_code)
    return redirect(obj.original_url)