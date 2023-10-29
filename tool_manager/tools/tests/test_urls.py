from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import ToolCreateView, ToolDeleteView, ToolDetailView, ToolListView, ToolUpdateView


class TestUrls(SimpleTestCase):
    def test_tool_list_is_resolved(self):
        url = reverse("tool")
        self.assertEqual(resolve(url).func.view_class, ToolListView)
        self.assertEqual(resolve(url).url_name, "tool")

    def test_tool_create_is_resolved(self):
        url = reverse("tool-create")
        self.assertEqual(resolve(url).func.view_class, ToolCreateView)
        self.assertEqual(resolve(url).url_name, "tool-create")

    def test_tool_update_is_resolved(self):
        url = reverse("tool-update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ToolUpdateView)
        self.assertEqual(resolve(url).url_name, "tool-update")

    def test_tool_detail_is_resolved(self):
        url = reverse("tool-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ToolDetailView)
        self.assertEqual(resolve(url).url_name, "tool-detail")

    def test_tool_delete_is_resolved(self):
        url = reverse("tool-delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ToolDeleteView)
        self.assertEqual(resolve(url).url_name, "tool-delete")
