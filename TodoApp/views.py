from django.shortcuts import render
from .models import Todo
from django.contrib import messages

# Create your views here.
def show(request):
    data=Todo.objects.all()
     
    return render(request, 'show.html', {'data':data})
    
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text'] 
        
        todo = Todo(title=title, text=text)
        todo.save()
        
        return render(request, 'add.html')
    else :
        return render(request, 'add.html')
    
def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    data=Todo.objects.all()
     
  
    messages.success(request, 'Item has been deleted.')
    return render(request, 'show.html', {'data':data})