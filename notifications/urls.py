from django.urls import path

from .views import UnreadNotificationListView, mark_notification_as_read

urlpatterns = [
    path(
        "unread-notifications/",
        UnreadNotificationListView.as_view(),
        name="unread-notifications",
    ),
    path("mark-as-read/<int:pk>/", mark_notification_as_read, name="mark-as-read"),
]
