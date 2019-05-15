from django.shortcuts import render

import os
import sys



# Create your views here.
def index(request):
    return render(request, 'index.html')

def test(request):
    print('asdfa;sdjgahsgasdjfkl;')
    os.system('python test.py')
    return render(request, 'index.html')
