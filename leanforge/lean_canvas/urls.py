from django.urls import path
from lean_canvas.views import (
    LeanCanvasListView,
    LeanCanvasDetailView,
    LeanCanvasCreateView,
    LeanCanvasUpdateView,
    LeanCanvasDeleteView,
)
from lean_canvas.views import (
    channel_update,
    channel_list,
    channel_detail,
    channel_create,
    channel_delete,
)
from lean_canvas.views import (
    cost_structure_create,
    cost_structure_list,
    cost_structure_update,
    cost_structure_delete,
    cost_structure_detail,
)


urlpatterns = [
    path("", LeanCanvasListView.as_view(), name="canvas_list"),
    path("<int:pk>/", LeanCanvasDetailView.as_view(), name="canvas_detail"),
    path("new/", LeanCanvasCreateView.as_view(), name="canvas_new"),
    path("<int:pk>/edit/", LeanCanvasUpdateView.as_view(), name="canvas_edit"),
    path(
        "<int:pk>/delete/",
        LeanCanvasDeleteView.as_view(),
        name="canvas_delete",
    ),
    # channels
    path(
        "<int:lean_canvas_id>/channels/",
        channel_list,
        name="channel_list",
    ),
    path("channels/<int:id>/", channel_detail, name="channel_detail"),
    path(
        "<int:lean_canvas_id>/channels/new/",
        channel_create,
        name="channel_create",
    ),
    path("channels/<int:id>/edit/", channel_update, name="channel_edit"),
    path("channels/<int:id>/delete/", channel_delete, name="channel_delete"),
    # cost_structures
    path(
        "<int:lean_canvas_id>/cost_structures/",
        cost_structure_list,
        name="cost_structure_list",
    ),
    path(
        "cost_structures/<int:id>/", cost_structure_detail, name="cost_structure_detail"
    ),
    path(
        "<int:lean_canvas_id>/cost_structures/new/",
        cost_structure_create,
        name="cost_structure_create",
    ),
    path(
        "cost_structures/<int:id>/edit/",
        cost_structure_update,
        name="cost_structure_update",
    ),
    path(
        "cost_structures/<int:id>/delete/",
        cost_structure_delete,
        name="cost_structure_delete",
    ),
]
