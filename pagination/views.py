from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
# Create your views here.
from .models import Employee
from rest_framework.decorators import api_view

# Hi Everyone

def get_data(request):
    emp = Employee.objects.all()
    print(emp)
    paginator = Paginator(emp, 5) # Show 5 emps per page.
    print(paginator.count)
    page_number = request.GET.get('page')  #2
    page_obj = paginator.get_page(page_number)
    context = {'employee': page_obj}
    return render(request, 'page.html', context)

@api_view(['POST'])
def save_data(request):
    data = request.data
    print(data, '@@@')
    if data.get('db'):
        Employee.objects.using(data.get('db')).create(name=data.get('name'), salary=data.get('salary'))
    else:
        Employee.objects.create(name=data.get('name'), salary=data.get('salary'))
    return HttpResponse('Employee created successfully...!')


def func():
    pass