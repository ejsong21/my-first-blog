from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User

# index
def index(request):
    return render(request, 'app/index.html')

# USER
def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'app/user_detail.html', {'user': user})
