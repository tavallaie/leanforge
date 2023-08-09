from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest

from lean_canvas.models import CostStructure, LeanCanvas
from lean_canvas.forms import CostStructureForm

# List
def cost_structure_list(request, lean_canvas_id):
    lean_canvas = get_object_or_404(LeanCanvas, id=lean_canvas_id)
    cost_structures = CostStructure.objects.filter(lean_canvas=lean_canvas)
    return render(
        request,
        "partials/cost_structures/cost_structure_list.html",
        {"cost_structures": cost_structures, "lean_canvas_id": lean_canvas_id},
    )


# Detail
def cost_structure_detail(request, id):
    cost_structure = get_object_or_404(CostStructure, id=id)
    return render(
        request,
        "partials/cost_structures/cost_structure_detail.html",
        {"cost_structure": cost_structure},
    )


# Create
def cost_structure_create(request, lean_canvas_id):
    if request.method == "GET":
        form = CostStructureForm()
        return render(
            request,
            "partials/cost_structures/cost_structure_form.html",
            {"form": form, "lean_canvas_id": lean_canvas_id},
        )
    elif request.method == "POST":
        lean_canvas = get_object_or_404(LeanCanvas, id=lean_canvas_id)
        form = CostStructureForm(request.POST)
        if form.is_valid():
            cost_structure = form.save(commit=False)
            cost_structure.lean_canvas = lean_canvas
            cost_structure.save()
            return redirect("cost_structure_list", lean_canvas_id=lean_canvas.id)
        return render(
            request,
            "partials/cost_structures/cost_structure_form.html",
            {"form": form, "lean_canvas_id": lean_canvas_id},
        )


# Update
def cost_structure_update(request, id):
    cost_structure = get_object_or_404(CostStructure, id=id)
    if request.method == "GET":
        form = CostStructureForm(instance=cost_structure)
        return render(
            request,
            "partials/cost_structures/cost_structure_form.html",
            {"form": form, "cost_structure": cost_structure},
        )
    elif request.method == "POST":
        form = CostStructureForm(request.POST, instance=cost_structure)
        if form.is_valid():
            form.save()
            return redirect("cost_structure_detail", id=cost_structure.id)
        return render(
            request,
            "partials/cost_structures/cost_structure_form.html",
            {"form": form, "cost_structure": cost_structure},
        )


# Delete
def cost_structure_delete(request, id):
    cost_structure = get_object_or_404(CostStructure, id=id)
    if request.method == "GET":
        return render(
            request,
            "partials/cost_structures/cost_structure_confirm_delete.html",
            {"cost_structure": cost_structure},
        )
    elif request.method == "POST":
        cost_structure.delete()
        return redirect(
            "cost_structure_list", lean_canvas_id=cost_structure.lean_canvas.id
        )
