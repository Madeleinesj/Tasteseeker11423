# tasteseeker/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import NewEntryForm
from .models import Cocktail
from django.contrib.auth import logout as auth_logout, login as auth_login  # avoid name collision
# from django.contrib.auth.decorators import login_required  # use if you want to protect pages

# -----------------------
# Public pages
# -----------------------

def Index(request):
    user = request.user
    context = {'user': user}
    return render(request, 'Index.html', context)

def AboutUs(request):
    return render(request, "AboutUs.html")

def login(request):
    # Render your login form page (this does not authenticate by itself)
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def logout(request):
    # Properly log the user out, then send them “home”
    auth_logout(request)
    # If your app is namespaced: 'tasteseeker:home' points to path('', views.Index, name='home')
    return redirect('tasteseeker:home')

# -----------------------
# Seeker pages
# -----------------------

def seeker_home(request):
    user = request.user
    context = {'user': user}
    return render(request, 'seeker_home.html', context)

def seeker_createentry(request):
    form = NewEntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # redirect by ROUTE NAME, not template file name
            return redirect('tasteseeker:seeker_drink_list')
    return render(request, 'seeker_createentry.html', {'form': form})

def seeker_drink_list(request):
    drink_list = Cocktail.objects.all()
    return render(request, 'seeker_drink_list.html', {'drink_list': drink_list})

def tasteseeker_search(request, pk):
    obj = get_object_or_404(Cocktail, pk=pk)
    return render(request, 'tasteseeker_search.html', {'obj': obj})

def edit_drink_details(request, pk):
    post = get_object_or_404(Cocktail, pk=pk)
    if request.method == 'POST':
        form = NewEntryForm(request.POST, instance=post)
        if form.is_valid():
            newform = form.save(commit=False)
            # If your model has an author field; otherwise remove next line
            newform.author = request.user
            newform.save()
            return redirect('tasteseeker:tasteseeker_search', pk=post.pk)
    else:
        form = NewEntryForm(instance=post)
    return render(request, 'edit_drink_details.html', {'form': form, 'post': post})

def seeker_deleteentry(request, pk):
    task = get_object_or_404(Cocktail, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasteseeker:seeker_drink_list')
    # Render a confirmation page (make sure this template exists)
    return render(request, 'seeker_deleteentry.html', {'task': task})
