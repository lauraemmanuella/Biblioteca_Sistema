from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .models import Usuario, Titulo, Exemplar, Emprestimo
from .forms import UsuarioForm, UsuarioEditForm, TituloForm, ExemplarForm, EmprestimoForm, DevolucaoForm


# Views para Home
def home(request):
    context = {
        'total_usuarios': Usuario.objects.count(),
        'total_titulos': Titulo.objects.count(),
        'total_exemplares': Exemplar.objects.count(),
        'emprestimos_ativos': Emprestimo.objects.filter(data_devolucao__isnull=True).count(),
        'emprestimos_em_atraso': Emprestimo.objects.filter(
            data_devolucao__isnull=True,
            previsao_devolucao__lt=timezone.now().date()
        ).count(),
    }
    return render(request, 'biblioteca/home.html', context)


# Views para Usuario
def usuario_list(request):
    search = request.GET.get('search', '')
    usuarios = Usuario.objects.all()
    
    if search:
        usuarios = usuarios.filter(
            Q(nome__icontains=search) | 
            Q(email__icontains=search) | 
            Q(telefone__icontains=search)
        )
    
    return render(request, 'biblioteca/usuario_list.html', {
        'usuarios': usuarios,
        'search': search
    })


def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    
    return render(request, 'biblioteca/usuario_form.html', {
        'form': form,
        'title': 'Criar Usuário'
    })


def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('usuario_list')
    else:
        form = UsuarioEditForm(instance=usuario)
    
    return render(request, 'biblioteca/usuario_form.html', {
        'form': form,
        'title': 'Editar Usuário',
        'usuario': usuario
    })


def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuário excluído com sucesso!')
        return redirect('usuario_list')
    
    return render(request, 'biblioteca/usuario_confirm_delete.html', {
        'usuario': usuario
    })


def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    emprestimos = usuario.emprestimos.all().order_by('-data_emprestimo')
    
    return render(request, 'biblioteca/usuario_detail.html', {
        'usuario': usuario,
        'emprestimos': emprestimos
    })


# Views para Titulo
def titulo_list(request):
    search = request.GET.get('search', '')
    titulos = Titulo.objects.all()
    
    if search:
        titulos = titulos.filter(
            Q(nome__icontains=search) | 
            Q(autor__icontains=search) | 
            Q(co_autor__icontains=search)
        )
    
    return render(request, 'biblioteca/titulo_list.html', {
        'titulos': titulos,
        'search': search
    })


def titulo_create(request):
    if request.method == 'POST':
        form = TituloForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Título criado com sucesso!')
            return redirect('titulo_list')
    else:
        form = TituloForm()
    
    return render(request, 'biblioteca/titulo_form.html', {
        'form': form,
        'title': 'Criar Título'
    })


def titulo_edit(request, pk):
    titulo = get_object_or_404(Titulo, pk=pk)
    
    if request.method == 'POST':
        form = TituloForm(request.POST, instance=titulo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Título atualizado com sucesso!')
            return redirect('titulo_list')
    else:
        form = TituloForm(instance=titulo)
    
    return render(request, 'biblioteca/titulo_form.html', {
        'form': form,
        'title': 'Editar Título',
        'titulo': titulo
    })


def titulo_delete(request, pk):
    titulo = get_object_or_404(Titulo, pk=pk)
    
    if request.method == 'POST':
        titulo.delete()
        messages.success(request, 'Título excluído com sucesso!')
        return redirect('titulo_list')
    
    return render(request, 'biblioteca/titulo_confirm_delete.html', {
        'titulo': titulo
    })


def titulo_detail(request, pk):
    titulo = get_object_or_404(Titulo, pk=pk)
    exemplares = titulo.exemplares.all()
    
    return render(request, 'biblioteca/titulo_detail.html', {
        'titulo': titulo,
        'exemplares': exemplares
    })


# Views para Exemplar
def exemplar_list(request):
    search = request.GET.get('search', '')
    exemplares = Exemplar.objects.select_related('id_titulo').all()
    
    if search:
        exemplares = exemplares.filter(
            Q(id_titulo__nome__icontains=search) | 
            Q(id_titulo__autor__icontains=search)
        )
    
    return render(request, 'biblioteca/exemplar_list.html', {
        'exemplares': exemplares,
        'search': search
    })


def exemplar_create(request):
    if request.method == 'POST':
        form = ExemplarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exemplar criado com sucesso!')
            return redirect('exemplar_list')
    else:
        form = ExemplarForm()
    
    return render(request, 'biblioteca/exemplar_form.html', {
        'form': form,
        'title': 'Criar Exemplar'
    })


def exemplar_edit(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    
    if request.method == 'POST':
        form = ExemplarForm(request.POST, instance=exemplar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exemplar atualizado com sucesso!')
            return redirect('exemplar_list')
    else:
        form = ExemplarForm(instance=exemplar)
    
    return render(request, 'biblioteca/exemplar_form.html', {
        'form': form,
        'title': 'Editar Exemplar',
        'exemplar': exemplar
    })


def exemplar_delete(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    
    if request.method == 'POST':
        exemplar.delete()
        messages.success(request, 'Exemplar excluído com sucesso!')
        return redirect('exemplar_list')
    
    return render(request, 'biblioteca/exemplar_confirm_delete.html', {
        'exemplar': exemplar
    })


def exemplar_detail(request, pk):
    exemplar = get_object_or_404(Exemplar, pk=pk)
    emprestimos = exemplar.emprestimos.all().order_by('-data_emprestimo')
    
    return render(request, 'biblioteca/exemplar_detail.html', {
        'exemplar': exemplar,
        'emprestimos': emprestimos
    })


# Views para Emprestimo
def emprestimo_list(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    
    emprestimos = Emprestimo.objects.select_related('id_usuario', 'id_exemplar__id_titulo').all()
    
    if search:
        emprestimos = emprestimos.filter(
            Q(id_usuario__nome__icontains=search) | 
            Q(id_exemplar__id_titulo__nome__icontains=search)
        )
    
    if status == 'ativo':
        emprestimos = emprestimos.filter(data_devolucao__isnull=True)
    elif status == 'devolvido':
        emprestimos = emprestimos.filter(data_devolucao__isnull=False)
    elif status == 'atrasado':
        emprestimos = emprestimos.filter(
            data_devolucao__isnull=True,
            previsao_devolucao__lt=timezone.now().date()
        )
    
    emprestimos = emprestimos.order_by('-data_emprestimo')
    
    return render(request, 'biblioteca/emprestimo_list.html', {
        'emprestimos': emprestimos,
        'search': search,
        'status': status
    })


def emprestimo_create(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empréstimo criado com sucesso!')
            return redirect('emprestimo_list')
    else:
        form = EmprestimoForm()
    
    return render(request, 'biblioteca/emprestimo_form.html', {
        'form': form,
        'title': 'Criar Empréstimo'
    })


def emprestimo_edit(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empréstimo atualizado com sucesso!')
            return redirect('emprestimo_list')
    else:
        form = EmprestimoForm(instance=emprestimo)
    
    return render(request, 'biblioteca/emprestimo_form.html', {
        'form': form,
        'title': 'Editar Empréstimo',
        'emprestimo': emprestimo
    })


def emprestimo_delete(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    
    if request.method == 'POST':
        emprestimo.delete()
        messages.success(request, 'Empréstimo excluído com sucesso!')
        return redirect('emprestimo_list')
    
    return render(request, 'biblioteca/emprestimo_confirm_delete.html', {
        'emprestimo': emprestimo
    })


def emprestimo_detail(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    
    return render(request, 'biblioteca/emprestimo_detail.html', {
        'emprestimo': emprestimo
    })


def emprestimo_devolver(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    
    if emprestimo.data_devolucao:
        messages.warning(request, 'Este empréstimo já foi devolvido!')
        return redirect('emprestimo_detail', pk=pk)
    
    if request.method == 'POST':
        form = DevolucaoForm(request.POST)
        if form.is_valid():
            emprestimo.devolver()
            messages.success(request, 'Exemplar devolvido com sucesso!')
            return redirect('emprestimo_detail', pk=pk)
    else:
        form = DevolucaoForm()
    
    return render(request, 'biblioteca/emprestimo_devolver.html', {
        'form': form,
        'emprestimo': emprestimo
    })
