# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Note
from .forms import NoteForm

@login_required
def note_list(request):
    # Shows all notes belonging to the logged-in user [cite: 39]
    notes = Note.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'note_list.html', {'notes': notes})

@login_required
def note_create(request):
    # Renders and processes the NoteForm for new notes [cite: 40]
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_edit(request, id):
    # Pre-populates NoteForm with existing note data [cite: 41]
    note = get_object_or_404(Note, id=id, owner=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_delete(request, id):
    # Asks for confirmation, then deletes [cite: 42]
    note = get_object_or_404(Note, id=id, owner=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})

def register_view(request):
    # Handles new user registration [cite: 43]
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})