from django.shortcuts import render
from .forms import Field
def index(request):
    result = ''
    form = Field(request.POST)
    if form.is_valid():
        result = form['content'].value()
    return render(request , 'core/index.html' , {'form':form , 'result':result})
