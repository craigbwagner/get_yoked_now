from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Workout


def home(request):
    return render(request, "home.html")


def workouts_index(request):
    workouts = Workout.objects.all()
    return render(request, "workouts/index.html", {"workouts": workouts})
