from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import (HolderListView, HolderUpdateView, HolderDetailView, HolderCreateView, HolderDeleteView,
                     ToolListView, ToolUpdateView, ToolDetailView, ToolDeleteView, ToolCreateView,
                     ToolAssemblyListView, ToolAssemblyCreateView, ToolAssemblyDeleteView, ToolAssemblyUpdateView,
                     ToolAssemblyDetailView, ToolAssemblyAddCommentView)


class TestUrls(SimpleTestCase):

    def test_holder_list_is_resolved(self):
        url = reverse('holder')
        self.assertEqual(resolve(url).func.view_class, HolderListView)
        self.assertEqual(resolve(url).url_name, 'holder')

    def test_holder_create_is_resolved(self):
        url = reverse('holder-create')
        self.assertEqual(resolve(url).func.view_class, HolderCreateView)
        self.assertEqual(resolve(url).url_name, 'holder-create')

    def test_holder_update_is_resolved(self):
        url = reverse('holder-update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, HolderUpdateView)
        self.assertEqual(resolve(url).url_name, 'holder-update')

    def test_holder_detail_is_resolved(self):
        url = reverse('holder-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, HolderDetailView)
        self.assertEqual(resolve(url).url_name, 'holder-detail')

    def test_holder_delete_is_resolved(self):
        url = reverse('holder-delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, HolderDeleteView)
        self.assertEqual(resolve(url).url_name, 'holder-delete')

    def test_tool_list_is_resolved(self):
        url = reverse('tool')
        self.assertEqual(resolve(url).func.view_class, ToolListView)
        self.assertEqual(resolve(url).url_name, 'tool')

    def test_tool_create_is_resolved(self):
        url = reverse('tool-create')
        self.assertEqual(resolve(url).func.view_class, ToolCreateView)
        self.assertEqual(resolve(url).url_name, 'tool-create')

    def test_tool_update_is_resolved(self):
        url = reverse('tool-update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ToolUpdateView)
        self.assertEqual(resolve(url).url_name, 'tool-update')

    def test_tool_detail_is_resolved(self):
        url = reverse('tool-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ToolDetailView)
        self.assertEqual(resolve(url).url_name, 'tool-detail')

    def test_tool_delete_is_resolved(self):
        url = reverse('tool-delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ToolDeleteView)
        self.assertEqual(resolve(url).url_name, 'tool-delete')

    def test_tool_assembly_list_is_resolved(self):
        url = reverse('tool-assembly')
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyListView)
        self.assertEqual(resolve(url).url_name, 'tool-assembly')

    def test_tool_assembly_create_is_resolved(self):
        url = reverse('tool-assembly-create')
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyCreateView)
        self.assertEqual(resolve(url).url_name, 'tool-assembly-create')

    def test_tool_assembly_update_is_resolved(self):
        url = reverse('tool-assembly-update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyUpdateView)
        self.assertEqual(resolve(url).url_name, 'tool-assembly-update')

    def test_tool_assembly_detail_is_resolved(self):
        url = reverse('tool-assembly-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyDetailView)
        self.assertEqual(resolve(url).url_name, 'tool-assembly-detail')

    def test_tool_assembly_delete_is_resolved(self):
        url = reverse('tool-assembly-delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyDeleteView)
        self.assertEqual(resolve(url).url_name, 'tool-assembly-delete')

    def test_tool_assembly_add_comment_is_resolved(self):
        url = reverse('add-comment', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ToolAssemblyAddCommentView)
        self.assertEqual(resolve(url).url_name, 'add-comment')
