from django.shortcuts import render

# Create your views here.

def about2(request):
    pangalan = 'Rachel'
    apelyido = 'Laeddis'
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


    return render(request, "about.html", {'fname':pangalan, 'lname':apelyido, 'age':edad, 'motto':kasabihan, 'snumber':snumber, 'aboutme': info})
