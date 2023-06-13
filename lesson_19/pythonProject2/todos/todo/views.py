from django.http import JsonResponse
from .models import Todo


def todo(request):
    todo_date = [todo for todo in Todo.objects.all().values('id', 'name', 'description', 'user', 'completed')]
    return JsonResponse({'posts': todo_date})
