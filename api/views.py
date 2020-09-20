import json

from django.shortcuts import render
from django.http import HttpResponse

from .sample import get_source
from .models import Employee, ActivityPeriods

# Create your views here.


def index(request):
    employee = Employee.objects.all()
    return render(request, 'api/index.html', {"employee_list": employee})


def read_data_from_file(request):
    # with open(r'api/json_data_file.json', 'r') as outfile:
    #     print(outfile)
    #     lines = outfile.readlines()
    #     data = json.load(outfile)
    #     print(lines)
        # print(type(lines))
        # data = "\n".join(lines)
        # return HttpResponse(data)
    get_source('api/json_data_file')

    return HttpResponse("success")
