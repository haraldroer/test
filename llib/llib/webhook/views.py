import os
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def index(request):

    jsondata = request.body

    f=open("debug.txt", "ab")
    f.write(jsondata + os.linesep.encode('ascii'))
    #f.write(os.linesep)
    f.close()
    return HttpResponse(status=200)