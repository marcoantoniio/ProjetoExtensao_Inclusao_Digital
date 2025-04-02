from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

# Função para lidar com o processo de cadastro de um novo usuário
def cadastro(request):
    # Verifica se a requisição foi feita via método POST
    if request.method == 'POST':
        # Obtém os dados do formulário enviado via POST (username, email, password, password_confirm)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Verifica se as senhas fornecidas são iguais
        if password != password_confirm:
            # Caso as senhas não coincidam, exibe uma mensagem de erro e renderiza novamente a página de cadastro
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'cadastro.html')

        # Verifica se já existe um usuário com o mesmo nome de usuário
        if User.objects.filter(username=username).exists():
            # Caso o nome de usuário já esteja em uso, exibe uma mensagem de erro e renderiza novamente a página de cadastro
            messages.error(request, 'Nome de usuário já está em uso.')
            return render(request, 'cadastro.html')

        # Cria o novo usuário utilizando o método create_user (que segura a senha de forma segura)
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Exibe uma mensagem de sucesso após o cadastro
        messages.success(request, 'Cadastro realizado com sucesso! Agora você pode fazer login.')
        
        # Redireciona o usuário para a página inicial (ou página que representa a "home")
        return redirect('login')

    # Caso a requisição não seja POST (provavelmente GET), apenas renderiza a página de cadastro
    return render(request, 'cadastro.html')

# Função para lidar com o processo de login de um novo usuário
def login_view(request):
    if request.method == 'POST':
        # Obtém o nome de usuário e a senha do formulário
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Tenta autenticar o usuário
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Se o usuário for autenticado, faz o login e redireciona
            login(request, user)
            return redirect('inicio')  # Redireciona para a URL 'inicio' após o login
        else:
            # Caso as credenciais sejam inválidas, exibe uma mensagem de erro
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('login')  # Redireciona de volta para a página de login

    return render(request, 'login.html')  # Exibe o formulário de login
