from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

def home(request):
    return render(request, 'users/home.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form})

def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'users/delete_user.html', {'user': user})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
