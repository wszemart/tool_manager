from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from .models import UserNotification


class UnreadNotificationListView(TemplateView):
    template_name = "notifications/unread_notification.html"
    context_object_name = "user_notifications"
    paginate_by = 15


@login_required
def mark_notification_as_read(request: HttpRequest, pk: int) -> HttpResponse:
    user_notification = get_object_or_404(UserNotification, pk=pk, is_read=False)

    if request.user != user_notification.notification.user:
        user_notification.is_read = True
        user_notification.save()

    return redirect("unread-notifications")
