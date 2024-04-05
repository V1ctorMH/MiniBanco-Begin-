from django.shortcuts import render
from .models import Usuario
from .models import Pagamentos

def Banco(request):
    return render(request,'DressBank/index.html')


def deletar_dados(request):
    Usuario.objects.all().delete()
    return render(request, 'DressBank/index.html')  # ou redirecione para outra página após a exclusão

def deletar_dados_pix(request):
    Pagamentos.objects.all().delete()
    return render(request, 'DressBank/Pix.html')  # ou redirecione para outra página após a exclusão

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.NdaConta = request.POST.get('NdaConta')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.saldo = request.POST.get('saldo')
    Usuario_id = 1
    novo_usuario.save()
    usuarios = {
            'usuarios': Usuario.objects.all()
        }
    return render(request,'DressBank/Menu.html', usuarios)

def Home(request):
    Usuario_id = 1
    usuarios = {
            'usuarios': Usuario.objects.all()
        }
    return render(request,'DressBank/Menu.html',usuarios)

def Menu(request):
    return render(request, 'DressBank/Menu.html')

def pixConta(request):
    return render(request, 'DressBank/Pix.html')

def Operacao(request):
    return render(request, 'DressBank/Operacoes.html')

def ListaPix(request):
    pagamento = {
            'pagamento': Pagamentos.objects.all()
        }
    return render(request,'DressBank/Listapix.html', pagamento)

def pagamento(request):
    novo_pix = Pagamentos()
    novo_pix.origem = request.POST.get('origem')
    novo_pix.dia = request.POST.get('dia')
    novo_pix.hora = request.POST.get('hora')
    novo_pix.destinovalor = request.POST.get('destinovalor')
    novo_pix.save()
    pagamento = {
            'pagamento': Pagamentos.objects.all()
        }
    return render(request,'DressBank/Listapix.html', pagamento)

def qr(request):
    return render(request, 'DressBank/qrcode.html')