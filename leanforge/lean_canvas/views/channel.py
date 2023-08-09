from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest

from lean_canvas.models import Channel, LeanCanvas
from lean_canvas.forms import ChannelForm


def channel_list(request, lean_canvas_id):
    lean_canvas = get_object_or_404(LeanCanvas, id=lean_canvas_id)
    channels = Channel.objects.filter(lean_canvas=lean_canvas)
    return render(
        request,
        "partials/channels/channel_list.html",
        {"channels": channels, "lean_canvas_id": lean_canvas_id},
    )


def channel_detail(request, id):
    channel = get_object_or_404(Channel, id=id)
    return render(
        request, "partials/channels/channel_detail.html", {"channel": channel}
    )


def channel_create(request, lean_canvas_id):
    if request.method == "GET":
        form = ChannelForm()
        return render(
            request,
            "partials/channels/channel_form.html",
            {"form": form, "lean_canvas_id": lean_canvas_id},
        )
    elif request.method == "POST":
        lean_canvas = get_object_or_404(LeanCanvas, id=lean_canvas_id)
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.lean_canvas = lean_canvas
            channel.save()
            return redirect("channel_list", lean_canvas_id=lean_canvas.id)
        return render(
            request,
            "partials/channels/channel_form.html",
            {"form": form, "lean_canvas_id": lean_canvas_id},
        )


def channel_update(request, id):
    if request.method == "POST":
        new_channel_name = request.POST.get("channel_name")
        channel = get_object_or_404(Channel, id=id)
        channel.channel = new_channel_name
        channel.save()

        # Return the updated channel's HTML representation
        return render(
            request, "partials/channels/channel_partial.html", {"channel": channel}
        )

    return HttpResponseBadRequest("Invalid request method")


def channel_delete(request, id):
    channel = get_object_or_404(Channel, id=id)
    if request.method == "GET":
        return render(
            request,
            "partials/channels/channel_confirm_delete.html",
            {"channel": channel},
        )
    elif request.method == "POST":
        channel.delete()
        return redirect(
            "partials/channels/channel_list", lean_canvas_id=channel.lean_canvas.id
        )
