import logging
from typing import Dict, List, Union

from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from .forms import CustomUserCreationForm, UserUpdateForm

logger = logging.getLogger(__name__)


class NewUserRegister(View):
    template_name: str = "users/register.html"

    def get(self, request) -> render:
        form = CustomUserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request) -> Union[render, redirect]:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account's been created for {username}!")
            logger.info(f"Account's been created for {username}!")
            return redirect("login")
        return render(request, self.template_name, {"form": form})


class LogoutUser(View):
    def get(self, request) -> redirect:
        user = request.user
        auth_logout(request)

        message: str = "You have been successfully logged out"
        messages.success(request, message)
        logger.info(f"{user} have been successfully logged out")

        return redirect("login")


class UserProfile(LoginRequiredMixin, View):
    template_name: str = "users/profile.html"

    def get(self, request) -> render:
        user_form = UserUpdateForm(instance=request.user)
        breadcrumbs: List[Dict] = [
            {"title": "Strona główna", "url": reverse("app-home")},
            {"title": "Profil użytkownika", "url": reverse("profile")},
        ]
        context: Dict = {"user_form": user_form, "breadcrumbs": breadcrumbs}
        return render(request, self.template_name, context)

    def post(self, request) -> Union[redirect, render]:
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your profile has been updated")
            logger.info(f"{request.user} profile has been updated.")
            return redirect("profile")
        logger.error(user_form.errors)
        messages.error(request, "There was an error updating your profile")
        return redirect("profile")
