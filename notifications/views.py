from django.shortcuts import render
from .models import Notification, UserNotification
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class UnreadNotificationListView(ListView):
    model = UserNotification
    template_name = 'notifications/unread_notification.html'
    context_object_name = 'user_notifications'
    paginate_by = 5

    # def get_queryset(self):
    #     user = self.request.user
    #     return UserNotification.objects.exclude(user=user).filter(is_read=False).select_related('notification__user_comment').order_by('-notification__created_at')

    def get_queryset(self):
        user = self.request.user
        return UserNotification.objects.filter(is_read=False).select_related(
            'notification__user_comment').order_by('-notification__created_at').exclude(user=user)


@login_required
def mark_notification_as_read(request, pk):
    user_notification = get_object_or_404(UserNotification, pk=pk, is_read=False)

    if request.user != user_notification.notification.user:
        user_notification.is_read = True
        user_notification.save()

    return redirect('unread-notifications')



