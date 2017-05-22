from django.shortcuts import render, HttpResponse
import random
VALUES = ['suprise motherfucka', 'sunrise motherfucka', 'all rise motherfucka', 'some fries motherfucka', 'booogity boogity boo']


# Create your views here.

def index(request):
    context={}
    return render(request, 'suprise_me/index.html')


def results(request):
    random.shuffle(VALUES)
    your_suprises =[]
    for x in range(int(request.POST['number'])):
        your_suprises.append(VALUES[x])
    context = {'your_suprises' : your_suprises}
    print context
    return render(request, 'suprise_me/results.html', context)
    print 'asdfaf'
