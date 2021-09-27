from django.http import HttpResponse
from django.template import loader


def Inicio(request):
    doc_login = loader.get_template('index.html')
    documento = doc_login.render()
    return HttpResponse(documento)
