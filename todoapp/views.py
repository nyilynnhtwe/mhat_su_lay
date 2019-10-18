from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import todoItem

def todoView(request):
    #this is for display
    all_todo_items=todoItem.objects.all()
    return render(request,'tempalte.html',{'all_items':all_todo_items})
    
def addtodo(request):
#this is for adding items
    new_item=todoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo')


def deletetodo(request,todo_id):
#this is for deleting items
    item_delete=todoItem.objects.get(id=todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/todo')