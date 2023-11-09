from django.urls import reverse

from holders.views import HolderCreateView, HolderDetailView, HolderListView, HolderUpdateView
from tools.views import ToolCreateView, ToolDetailView, ToolListView, ToolUpdateView

from .views import ToolAssemblyCreateView, ToolAssemblyDetailView, ToolAssemblyListView, ToolAssemblyUpdateView

BREADCRUMB_CONFIG = {
    # HolderListView: [{"title": "Lista oprawek", "url": reverse("holder")}],
    # HolderDetailView: [
    #     {
    #         "title": lambda obj: obj.get_holder_type_display,
    #         "url": reverse("holder-detail", kwargs={"pk": {"pk"}}),
    #     }
    # ],
    # HolderUpdateView: [{"title": "Aktualizuj", "url": reverse("holder-update", kwargs={"pk": {"pk"}})}],
    # HolderCreateView: [{"title": "Utwórz nową oprawkę", "url": reverse("holder-create")}],
    # ToolListView: [{"title": "Lista frezów", "url": reverse("tool")}],
    # ToolDetailView: [
    #     {
    #         "title": lambda obj: obj.get_tool_type_display,
    #         "url": reverse("tool-detail", kwargs={"pk": {"pk"}}),
    #     }
    # ],
    # ToolUpdateView: [{"title": "Aktualizuj", "url": reverse("tool-update", kwargs={"pk": {"pk"}})}],
    # ToolCreateView: [{"title": "Utwórz nowy frez", "url": reverse("tool-create")}],
    ToolAssemblyListView: [{"title": "Lista narzędzi", "url": reverse("tool-assembly")}],
    ToolAssemblyDetailView: [
        {
            "title": lambda obj: f"T{obj.tool_nr} R{obj.tool_assembly.radius} {obj.tool_assembly.tool.get_tool_type_display()}",  # noqa: E501
            "url": reverse("tool-assembly-detail", kwargs={"pk": "{pk}"}),
        }
    ],
    # ToolAssemblyUpdateView: [
    #     {
    #         "title": "Aktualizuj",
    #         "url": reverse("tool-assembly-update", kwargs={"pk": "{pk}"}),
    #     }
    # ],
    ToolAssemblyCreateView: [{"title": "Utwórz nowe narzędzie", "url": reverse("tool-assembly-create")}],
}
