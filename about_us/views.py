# views.py
from django.shortcuts import render

from accounts.models import User


def about_us(request):
    users = User.objects.all()  # Fetch all users from the database
    return render(request, 'about_us.html', {'users': users})