from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account's been created for {username}!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def logout(request):
    auth_logout(request)

    message = 'You have been successfully logged out!'
    messages.success(request, message)

    return redirect('login')


@login_required
def profile(request):
    user_form = UserUpdateForm(instance=request.user)

    if request.method == "POST":
        if request.user == request.user.profile.user:
            user_form = UserUpdateForm(request.POST, instance=request.user)

            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Your profile's been updated")
                return redirect('profile')
            else:
                messages.error(request, "You are not authorized to edit this profile.")

    breadcrumbs = [{'title': 'Strona główna', 'url': reverse('app-home')},
                   {'title': 'Profil użytkownika', 'url': reverse('profile')}]

    context = {
        'user_form': user_form,
        'breadcrumbs': breadcrumbs,
    }

    return render(request, 'users/profile.html', context)

