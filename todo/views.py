from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import ToDoList, ToDoItem


# Create your views here.
class CreateToDosView(CreateView):
    model = ToDoList
    fields = ['title']
    template_name = 'todo/list_add.html'

    def get_context_data(self, **kwargs):
        context = super(CreateToDosView, self).get_context_data()
        context['title'] = "Add a new list!"
        return context


class CreateItemView(CreateView):
    model = ToDoItem
    fields = ['title', 'description', 'due_date', 'todo_list']
    template_name = 'todo/item_add.html'

    def get_initial(self):
        initial_data = super(CreateItemView, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list'] = todo_list
        return initial_data

    def get_context_data(self, **kwargs):
        context = super(CreateItemView, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        context['title'] = 'Create a new item!'
        return context

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])


class ListToDosView(ListView):
    model = ToDoList
    template_name = 'todo/index.html'


class ListItemsView(ListView):
    model = ToDoItem
    template_name = 'todo/todo_list.html'

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs['list_id'])

    def get_context_data(self):
        context = super().get_context_data()
        context['todo_list'] = ToDoList.objects.get(id=self.kwargs['list_id'])
        return context


class UpdateItemsView(UpdateView):
    model = ToDoItem
    fields = ['title', 'description', 'due_date', 'todo_list']
    template_name = 'todo/item_add.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateItemsView, self).get_context_data()
        context['todo_list'] = self.object.todo_list
        context['title'] = 'Edit item'
        return context

    def get_success_url(self):
        return reverse('list', args=[self.object.todo_list_id])


class DeleteToDosView(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('index')


class DeleteItemsView(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse('list', args=[self.kwargs['list_id']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['todo_list'] = self.object.todo_list
        return context