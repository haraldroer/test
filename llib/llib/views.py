from django.http import HttpResponse

# importing loading from django template
from django.template import loader


# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('index.html')

    #creating the values to pass
    context = {
        'instruction':'Belal Khan',
    }
    
    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))
