from django.shortcuts import render, redirect

from forum.forms import CreateInForum, CreateInDiscussion
from forum.models import Forum


def home(request):
    forums = Forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'home.html', context)


def add_in_forum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'add_in_forum.html', context)


def add_in_discussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'add_in_discussion.html', context)
