# Sistema de Gestão de Biblioteca

Um sistema completo de gestão de biblioteca desenvolvido em Python com Django e SQLite.

## Funcionalidades

### Gestão de Usuários
- Cadastro de usuários com nome, telefone, email e senha
- Listagem, edição e exclusão de usuários
- Visualização de histórico de empréstimos por usuário
- Sistema de busca por nome, email ou telefone

### Gestão de Títulos
- Cadastro de títulos com nome, autor e co-autor (opcional)
- Listagem, edição e exclusão de títulos
- Visualização de exemplares por título
- Sistema de busca por título, autor ou co-autor

### Gestão de Exemplares
- Cadastro de exemplares vinculados a títulos
- Geração automática de QR Code para cada exemplar
- Controle de disponibilidade (disponível/emprestado)
- Listagem, edição e exclusão de exemplares

### Gestão de Empréstimos
- Registro de empréstimos com usuário, exemplar e previsão de devolução
- Controle automático de disponibilidade dos exemplares
- Sistema de devolução com registro de data/hora
- Identificação de empréstimos em atraso
- Filtros por status (ativo, devolvido, em atraso)
- Histórico completo de empréstimos

## Estrutura do Banco de Dados

### Usuario
- `id_usuario` (PK): ID único do usuário
- `nome`: Nome completo
- `telefone`: Número de telefone
- `email`: Email (único)
- `senha`: Senha criptografada

### Titulo
- `id_titulo` (PK): ID único do título
- `nome`: Nome do título/livro
- `autor`: Autor principal
- `co_autor`: Co-autor (opcional)
- `data_cadastro`: Data de cadastro automática

### Exemplar
- `id_exemplar` (PK): ID único do exemplar
- `id_titulo` (FK): Referência ao título
- `data_aquisicao`: Data de aquisição
- `qrcode_data`: QR Code em base64 (gerado automaticamente)
- `disponivel`: Status de disponibilidade

### Emprestimo
- `id_emprestimo` (PK): ID único do empréstimo
- `id_usuario` (FK): Referência ao usuário
- `id_exemplar` (FK): Referência ao exemplar
- `data_emprestimo`: Data/hora do empréstimo
- `previsao_devolucao`: Data prevista para devolução
- `data_devolucao`: Data/hora da devolução (opcional)

## Tecnologias Utilizadas

- **Python 3.11**: Linguagem de programação
- **Django 5.2.6**: Framework web
- **SQLite**: Banco de dados
- **Bootstrap 5.3**: Framework CSS
- **Bootstrap Icons**: Ícones
- **QRCode**: Geração de códigos QR

## Como Executar

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone ou baixe o projeto**
   ```bash
   cd biblioteca_sistema
   ```

2. **Instale as dependências**
   ```bash
   pip install django qrcode[pil]
   ```

3. **Execute as migrações**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Inicie o servidor**
   ```bash
   python manage.py runserver
   ```

5. **Acesse o sistema**
   Abra o navegador e acesse: `http://localhost:8000`

### Criando um Superusuário (Opcional)

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

Depois acesse: `http://localhost:8000/admin`

## Estrutura do Projeto

```
biblioteca_sistema/
├── biblioteca/                 # App principal
│   ├── migrations/            # Migrações do banco
│   ├── templates/             # Templates HTML
│   │   └── biblioteca/        # Templates do app
│   ├── models.py              # Modelos do banco
│   ├── views.py               # Views/controladores
│   ├── forms.py               # Formulários
│   └── urls.py                # URLs do app
├── biblioteca_sistema/        # Configurações do projeto
│   ├── settings.py            # Configurações
│   └── urls.py                # URLs principais
├── db.sqlite3                 # Banco de dados SQLite
└── manage.py                  # Script de gerenciamento
```

## Funcionalidades Implementadas

### ✅ CRUD Completo
- **C**reate: Criação de usuários, títulos, exemplares e empréstimos
- **R**ead: Listagem e visualização detalhada de todos os registros
- **U**pdate: Edição de todos os tipos de registro
- **D**elete: Exclusão com confirmação

### ✅ Recursos Avançados
- Sistema de busca em todas as listagens
- Geração automática de QR Codes para exemplares
- Controle automático de disponibilidade
- Identificação de empréstimos em atraso
- Interface responsiva e moderna
- Mensagens de feedback para o usuário
- Validação de formulários
- Criptografia de senhas

### ✅ Interface de Usuário
- Design moderno com Bootstrap 5
- Navegação intuitiva com menus dropdown
- Painel de controle com estatísticas
- Ações rápidas na página inicial
- Tabelas responsivas com ações
- Formulários bem estruturados
- Confirmações de exclusão

## Uso do Sistema

### 1. Página Inicial
- Visualize estatísticas gerais do sistema
- Acesse ações rápidas para cadastros
- Navegue pelos menus principais

### 2. Gestão de Usuários
- Cadastre novos usuários com dados completos
- Busque usuários por nome, email ou telefone
- Visualize histórico de empréstimos de cada usuário

### 3. Gestão de Títulos
- Adicione novos títulos ao acervo
- Inclua autor e co-autor quando aplicável
- Visualize todos os exemplares de um título

### 4. Gestão de Exemplares
- Cadastre exemplares físicos dos títulos
- Cada exemplar recebe um QR Code único
- Controle automático de disponibilidade

### 5. Gestão de Empréstimos
- Registre novos empréstimos facilmente
- Apenas exemplares disponíveis são exibidos
- Processe devoluções com um clique
- Monitore empréstimos em atraso

## Observações Importantes

- O sistema usa SQLite como banco de dados, ideal para desenvolvimento e pequenas instalações
- As senhas são criptografadas automaticamente
- QR Codes são gerados automaticamente para cada exemplar
- O sistema controla automaticamente a disponibilidade dos exemplares
- Empréstimos em atraso são identificados automaticamente
- A interface é totalmente responsiva e funciona em dispositivos móveis

## Suporte

Este sistema foi desenvolvido como uma solução completa para gestão de bibliotecas pequenas e médias. Todas as funcionalidades CRUD foram implementadas e testadas com sucesso.

