from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello!")

def blog(request):
    return HttpResponse("Welcome to my Blog! ENJOY!")

def about2(request):
    pangalan = 'Rachel'
    apelyido = 'Paras'
    edad = '20'

    return render(request, "about2.html", {'fname':pangalan, 'lname':apelyido, 'age':edad})

def about(request):
    pangalan = 'Mae'
    apelyido = 'De Mesa'
    edad = '20'
    kasabihan = 'Live life to the fullest'
    snumber = 'A20-29378'
    info = 'Hi, I am currently a 3rd year BSIS with specialization in Business Analytics, I wanted to become a data analyst someday \
        or a project manager, But I hate programming subject'


    return render(request, "about.html", {'fname':pangalan, 'lname':apelyido, 'age':edad, 'motto':kasabihan, 'snumber':snumber, 'aboutme': info,})

def Score(request):
    
    quiz1 = '78'
    quiz2 = '85'
    quiz3 = '90'
    Fullname = 'Mae Dador De Mesa'
    
    return render(request, 'quiz.html', {'quiz1' : quiz1, 'quiz2' : quiz2, 'quiz3': quiz3, 'fnme' : Fullname,})