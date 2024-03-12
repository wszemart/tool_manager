from django.test import TestCase
from django.urls import reverse

from machines.factories import MachineFactory
from notifications.factories import NotificationFactory, UserNotificationFactory
from tools_assembly.factories import HolderFactory, ToolAssemblyFactory, ToolFactory, UserCommentFactory
from users.factories import UserFactory


class TestNotificationView(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user_1 = UserFactory()
        self.machine = MachineFactory()
        self.holder = HolderFactory(author=self.user)
        self.tool = ToolFactory(author=self.user)
        self.tool_assembly = ToolAssemblyFactory(author=self.user)
        self.user_comment = UserCommentFactory(author=self.user, tool_assembly=self.tool_assembly)
        self.notification = NotificationFactory(user=self.user, user_comment=self.user_comment)
        self.user_notification = UserNotificationFactory(user=self.user, notification=self.notification)

    def test_unread_notification_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("unread-notifications"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notifications/unread_notification.html")
        self.assertIn("user_notifications", response.context)
        self.assertTrue(response.context["user_notifications"].exists())

    def test_mark_notification_as_read_view(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse("mark-as-read", kwargs={"pk": self.user_notification.pk}))
        self.assertEqual(response.status_code, 302)
        self.user_notification.refresh_from_db()
        self.assertTrue(self.user_notification.is_read)
