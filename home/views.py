from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm


@login_required
def app(request):
    user_groups = Group.objects.filter(user=request.user)
    context = {
        'user': request.user,
        'groups': user_groups,
        'group_count': len(user_groups),
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    error_messages = []
    if form.errors:
        for field in form.errors:
            for error in form.errors[field]:
                error_messages.append(error)
    return render(request, 'register.html', {'form': form, 'error_messages': error_messages})


def room(request, room_name):
    return render(request, 'group.html', {
        'room_name': room_name
    })