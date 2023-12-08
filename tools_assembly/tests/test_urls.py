from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import (
    ToolAssemblyAddCommentView,
    ToolAssemblyCreateView,
    ToolAssemblyDeleteView,
    ToolAssemblyDetailView,
    ToolAssemblyListView,
    ToolAssemblyUpdateView,
)


class TestUrls(SimpleTestCase):
    def test_tool_assembly_list_is_resolved(self):
        url = reverse("tool-assembly")
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyListView)
        self.assertEqual(resolve(url).url_name, "tool-assembly")

    def test_tool_assembly_create_is_resolved(self):
        url = reverse("tool-assembly-create")
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyCreateView)
        self.assertEqual(resolve(url).url_name, "tool-assembly-create")

    def test_tool_assembly_update_is_resolved(self):
        url = reverse("tool-assembly-update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyUpdateView)
        self.assertEqual(resolve(url).url_name, "tool-assembly-update")

    def test_tool_assembly_detail_is_resolved(self):
        url = reverse("tool-assembly-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyDetailView)
        self.assertEqual(resolve(url).url_name, "tool-assembly-detail")

    def test_tool_assembly_delete_is_resolved(self):
        url = reverse("tool-assembly-delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyDeleteView)
        self.assertEqual(resolve(url).url_name, "tool-assembly-delete")

    def test_tool_assembly_add_comment_is_resolved(self):
        url = reverse("add-comment", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyAddCommentView)
        self.assertEqual(resolve(url).url_name, "add-comment")
