from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import UnreadNotificationListView, mark_notification_as_read


class TestUrls(SimpleTestCase):

    def test_mark_notification_as_read_is_resolved(self):
        url = reverse('mark-as-read', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, mark_notification_as_read)

    def test_notification_list_is_resolved(self):
        url = reverse('unread-notifications')
        self.assertEqual(resolve(url).func.view_class, UnreadNotificationListView)
        self.assertEqual(resolve(url).url_name, 'unread-notifications')
