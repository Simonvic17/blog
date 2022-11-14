from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UsersCreateForm, UserUpdateForm


def register(request):
    if request.method == "POST":
        form = UsersCreateForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'{first_name} your account is created, You are redirect to login page')
            return redirect('user:login')
    else:
        form = UsersCreateForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def profile_update(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile was updated')
            return redirect('user:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        "form": form, 
    }
    return render(request, 'user/profile_update.html', context)