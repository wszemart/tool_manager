from notifications.models import UserNotification

from .models import Machine


def all_machines(request):
    return {"machines": Machine.objects.all()}


def user_notifications(request):
    if not request.user.is_anonymous:
        user = request.user
        return {
            "user_notifications": UserNotification.objects.filter(user=user, is_read=False)
            .select_related("notification__user_comment")
            .order_by("-notification__created_at")
        }
    return {"user_notifications": []}
