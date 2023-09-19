from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Notification, UserNotification
from tools_assembly.models import UserComment, ToolAssembly, Tool, Holder
from machines.models import Machine
from django.test import Client


class TestNotificationView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.machine = Machine.objects.create(
            name='Test Machine',
            description='Test description'
        )
        self.holder = Holder.objects.create(holder_type='type_1', inner_diameter=25, author=self.user)
        self.tool = Tool.objects.create(tool_type='end_mill', catalog_nr='123', author=self.user)
        self.toolassembly = ToolAssembly.objects.create(
            tool_nr=1,
            radius=8,
            total_length=300,
            outside_holder=150,
            machine=self.machine,
            holder=self.holder,
            tool=self.tool,
            author=self.user
        )
        self.user_comment = UserComment.objects.create(content='testcomment', author=self.user, toolassembly=self.toolassembly)
        self.notification = Notification.objects.create(user=self.user, user_comment=self.user_comment)
        self.user_notification = UserNotification.objects.create(user=self.user, notification=self.notification)

    def test_unread_notification_list_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('unread-notifications'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notifications/unread_notification.html')
        self.assertIn('user_notifications', response.context)
        self.assertTrue(response.context['user_notifications'].exists())

    def test_mark_notification_as_read_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('mark-as-read', kwargs={'pk': self.user_notification.pk}))
        self.assertEqual(response.status_code, 302)
        self.user_notification.refresh_from_db()
        self.assertTrue(self.user_notification.is_read)
