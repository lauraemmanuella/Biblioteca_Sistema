from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
import qrcode
from io import BytesIO
import base64


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    
    def set_password(self, raw_password):
        self.senha = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Titulo(models.Model):
    id_titulo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=300)
    autor = models.CharField(max_length=200)
    co_autor = models.CharField(max_length=200, blank=True, null=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.nome} - {self.autor}"
    
    class Meta:
        verbose_name = "Título"
        verbose_name_plural = "Títulos"


class Exemplar(models.Model):
    id_exemplar = models.AutoField(primary_key=True)
    id_titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE, related_name='exemplares')
    data_aquisicao = models.DateField()
    qrcode_data = models.TextField(blank=True)
    disponivel = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.qrcode_data:
            # Gerar QR Code baseado no ID do exemplar
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr_text = f"Exemplar-{self.id_exemplar or 'TEMP'}-{self.id_titulo.nome if self.id_titulo else 'UNKNOWN'}"
            qr.add_data(qr_text)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            self.qrcode_data = img_str
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Exemplar {self.id_exemplar} - {self.id_titulo.nome}"
    
    class Meta:
        verbose_name = "Exemplar"
        verbose_name_plural = "Exemplares"


class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos')
    id_exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateTimeField(default=timezone.now)
    previsao_devolucao = models.DateField()
    data_devolucao = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Atualizar disponibilidade do exemplar
        if self.data_devolucao:
            self.id_exemplar.disponivel = True
        else:
            self.id_exemplar.disponivel = False
        self.id_exemplar.save()
        super().save(*args, **kwargs)
    
    def devolver(self):
        self.data_devolucao = timezone.now()
        self.id_exemplar.disponivel = True
        self.id_exemplar.save()
        self.save()
    
    @property
    def em_atraso(self):
        if not self.data_devolucao and self.previsao_devolucao < timezone.now().date():
            return True
        return False
    
    def __str__(self):
        status = "Devolvido" if self.data_devolucao else "Em empréstimo"
        return f"Empréstimo {self.id_emprestimo} - {self.id_usuario.nome} - {status}"
    
    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
