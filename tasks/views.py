from asyncio import Task, tasks
from http.client import HTTPResponse
from django.contrib.auth.decorators import login_required
from turtle import done, title
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import task
from .forms import taskform
from django.contrib import messages
import datetime

@login_required # Prqa acessa precisa está logado, te amo django
def tasklist(request):
    search = request.GET.get('search') # search é o nome do input de busca
    filter = request.GET.get('filter')
    taskDoneRecently = task.objects.filter(done='done', upadate_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    taskDone = task.objects.filter(done='done', user=request.user).count()
    taskDoing = task.objects.filter(done='doing', user=request.user).count()

    if search:
        tasks = task.objects.filter(title__icontains=search, user=request.user) #ico vai fazer a busca de acordo com oq tem no search pra não precisa escrever exatamente

    elif filter: 
        tasks = task.objects.filter(done=filter, user=request.user)

    else: # se não faz a paginação

        tasks_list = task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(tasks_list, 3) #Número q exibir por p´GINA
        page = request.GET.get('page')

        tasks = paginator.get_page(page) # Vai exbir o número na página que ele tá

    return render(request, 'tasks/list.html', {'tasks': tasks, 'taskDoneRecently': taskDoneRecently, 'taskDone': taskDone, 'taskDoing': taskDoing}) # As tasks q eu resgatei do banco

    
@login_required
def taskView(request, id):
    Task = get_object_or_404(task, pk=id) # Task é para informar o conteúdo pelo id task é o a view
    return render(request, 'tasks/task.html', {'task': Task}) # Resgatando do banco


def helloworld(request):
    return HttpResponse('Hello world')

@login_required
def newTask(request):
    if request.method == 'POST':
        form = taskform(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing' #Por padrão vai como doing
            task.user = request.user
            messages.success(request, 'Tarefa criada com sucesso.')
            task.save() # Depois salva
            return redirect('/')

    else:
        form = taskform()
        return render(request, 'tasks/addtask.html', {'form': form} )

@login_required
def editTask(request, id):
    Task = get_object_or_404(task, pk=id)
    form = taskform(instance=Task) # Tem q instanciar a variavel q pegou os objetos

    if request.method == 'POST':
        form = taskform(request.POST, instance=Task)

        if form.is_valid():
            Task.save() # Salvar a variavel da função
            messages.success(request, 'Tarefa editada com sucesso.')
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': Task})

    else: 
        return render(request, 'tasks/edittask.html', {'form': form, 'task': Task})

@login_required
def deleteTask(request, id):
    Task = get_object_or_404(task, pk=id)
    Task.delete()
    messages.success(request, 'Tarefa deletada.')
    return redirect('/')


@login_required
def changeStatus(request, id):
    Task= get_object_or_404(task, pk=id)

    if(Task.done == 'doing'):
        Task.done = 'done'
    else:
      Task.done = 'doing'

    Task.save()  
    messages.success(request, 'Status da tarefa alterado.')
    return redirect('/')

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})
