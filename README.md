# Sistema de Gestão de Biblioteca

Um sistema de gestão de biblioteca desenvolvido em Python com Django e SQLite.

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
   Abra o navegador e acesse: `http://localhost:8000` ou `http://127.0.0.1:8000`


