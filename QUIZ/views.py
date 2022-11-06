from django.shortcuts import render

# Create your views here.

def Score(request):
 
    quiz1 = '78',
    quiz2 =  '85',
    quiz3 = '90'
    Fullname = 'Mae Dador De Mesa'
    
    return render(request, 'quiz.html', {'quiz1' : quiz1, 'quiz2' : quiz2, 'quiz3': quiz3, 'fnme': Fullname,})
