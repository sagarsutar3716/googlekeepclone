from django.shortcuts import render,HttpResponse,redirect
from .models import Note


def note(request):
    notes =  Note.objects.order_by('-date_posted')

    context = {'notes':notes}

    if request.method == "POST":
       title = request.POST.get("title", "")
       note = request.POST.get("note", "")
       created_note = Note(title=title, note=note)
       created_note.save()
       return redirect('/') 

    return render(request, 'note.html', context)
   
def delete_note(request, id):
   if request.method == 'POST':
    remove = Note.objects.get(pk=id)
    remove.delete()
    return redirect('/')