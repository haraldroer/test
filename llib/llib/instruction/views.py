from django.http import HttpResponse
from llib.instruction.models import Instruction
from django.template import loader
import random
from django.http import JsonResponse



# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('index.html')

    #all obj
    max_id = Instruction.objects.all().count()
    ins = Instruction.objects.get(id=random.randint(1,max_id))

    # creating the values to pass
    context = {
        'instruction': ins.text,

}
    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))

def entry(request):
    # getting our template
    template = loader.get_template('entry.html')


    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))
def index2(request):
    #all obj
    max_id = Instruction.objects.all().count()
    ins = Instruction.objects.get(id=random.randint(1,max_id))

    response_data = {'text': ins.text}

    return JsonResponse(response_data)
