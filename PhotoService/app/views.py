from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Photo

# index
def index(request):
    return render(request, 'index.html')

# USER
def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})
