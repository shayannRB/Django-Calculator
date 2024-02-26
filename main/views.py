from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def main(request):

    number1  = request.POST.get('number1')
    number2  = request.POST.get('number2')
    opp  = request.POST.get('opperation')

    
    if opp == '*':
        number1 = int(number1)
        number2 = int(number2)

        result = number1 * number2
        return render(request, 'html2.html', context={'number' : str(result)}) 


    if opp == '-':
        number1 = int(number1)
        number2 = int(number2)

        result = number1 - number2
        return render(request, 'html2.html', context={'number' : str(result)}) 

    if opp == '+':
        number1 = int(number1)
        number2 = int(number2)

        result = number1 + number2
        return render(request, 'html2.html', context={'number' : str(result)}) 

    if opp == '/':
        number1 = int(number1)
        number2 = int(number2)

        result = number1 / number2
        return render(request, 'html2.html', context={'number' : str(result)}) 
    
    
    return render(request, 'html1.html', context={'number' : 'number'}) 
    
