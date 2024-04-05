from django.urls import path
from App_DressBank import views

urlpatterns = [
    path('', views.Banco, name='Banco'),
    path('DressBank/Conta/', views.usuarios, name='Listagem_Contas'),
    path('DressBank/PixLista/', views.pagamento, name='Listagem_Pix'),
    path('DressBank/DeletarDados', views.deletar_dados, name='deletar_dados'),
    path('DressBank/DeletarDadosPix/', views.deletar_dados_pix, name='deletar_dados_pix'),
    path('DressBank/Pix/', views.pixConta, name='Operacoes'),
    path('DressBank/Operações/', views.Operacao, name='PixOperacoes'),
    path('DressBank/Menu/', views.Home, name='ContaBanco'),
    path('DressBank/ListaPix/', views.ListaPix, name="ListaPix"),
    path('DressBank/Receber/', views.qr, name='Receber')
]