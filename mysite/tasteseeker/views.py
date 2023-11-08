from asyncio import Task

from django.shortcuts import render, redirect, get_object_or_404
from calendar import HTMLCalendar
from datetime import datetime, timezone
from .forms import NewEntryForm
from .models import Cocktail
from django.contrib.auth.decorators import login_required
import requests


def tasteseekerHome(request):
    user = request.user
    context = {'user': user}
    return render(request, 'tasteseeker_home.html', context)


def tasteseeker_createentry(request):
    form = NewEntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('tasteseeker_createentry.html')
    content = {'form': form}
    return render(request, 'tasteseeker_createentry.html', content)


def edit_drink_details(request, pk):
    pk = int(pk)
    post = get_object_or_404(Cocktail, pk=pk)
    form = NewEntryForm(request.POST or None, instance=post)
    if form.is_valid():
        newform = form.save(commit=False)
        newform.author = request.user
        newform.save()
        return redirect('tasteseeker_search', pk=post.pk)
    else:
        content = {'form': form, 'post': post}
        form = NewEntryForm(instance=post)
        return render(request, 'edit_drink_details.html', )


def tasteseeker_deleteentry(request, pk):
    pk = int(pk)
    task = get_object_or_404(Cocktail, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasteseeker_drink_list')
    content = {
        'task': task
    }

    return render(request, 'tasteseeker_drink_list', content)

def tasteseeker_drink_list(request):
    drink_list = Cocktail.objects.all()
    return render(request, 'tasteseeker_drink_list.html',
                  {'drink_list': drink_list})


def tasteseeker_search(request, pk):
    pk = int(pk)
    obj = Cocktail.objects.filter(pk=pk)
    context = {
        'obj': obj

    }
    return render(request, 'tasteseeker_search.html', context)


def LogIn(request):
    return render(request, "LogIn.html")