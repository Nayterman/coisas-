from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Teste")

def detail(request,question_id):
    return HttpResponse('yuiuiauijiaji'%question_id)
 
def detail(request,question_id):
    response='yuiuiauijiaji'
    return HttpResponse(response question_id)
