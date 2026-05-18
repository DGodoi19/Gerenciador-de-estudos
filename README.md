### A Solução
O **Gerenciador de Estudos Acadêmicos** é uma aplicação web desenvolvida em Django para organização e gerenciamento de tópicos de estudo e trilhas de aprendizagem. O projeto foca em auxiliar um estudante a gerenciar seus estudos, o que está aprendendo agora, e acompanhar seu progresso de uma maneira interativa, intuitiva, e com um visual atrativo e moderno (Tema Dark Purple).

---

## Link do Projeto em Produção (Deploy)

O sistema foi publicado em ambiente de produção e está totalmente operacional na nuvem através do link:  
**[Gerenciador de Estudos - Railway](http://gerenciador-de-estudos-production.up.railway.app/)**

---

## Tecnologias Utilizadas

- **Framework:** Django 4.2+
- **Linguagem:** Python 3.13 (Produção) / Python 3.12 (Local)
- **Banco de Dados:** PostgreSQL (Produção no Railway) / SQLite3 (Ambiente Local)
- **Integração Externa:** `requests` para consumo em tempo real da **BrasilAPI** (Exibição de Feriados Nacionais no Calendário)
- **Servidor de Produção & Estáticos:** Gunicorn & WhiteNoise
- **Qualidade de Código:** Ruff (Linting e Análise Estática)
- **Testes:** Pytest com `pytest-django`
- **CI/CD:** GitHub Actions

---

## Governança e Fluxo de Desenvolvimento (Git)

O projeto seguiu rigorosamente as boas práticas de Git Flow e Governança exigidas para o desenvolvimento de software:
1. **Planejamento:** Criação de Issues para mapear os requisitos da entrega.
2. **Ramificação:** Desenvolvimento isolado de novas features na branch `entrega-intermediaria`.
3. **Integração Contínua (CI):** Validação automatizada do código via GitHub Actions (Ruff e Pytest) a cada push, garantindo estabilidade antes da integração.
4. **Revisão e Integração:** Criação de Pull Request para revisão do código e realização do Merge para a branch principal (`main`).

---

## Funcionalidades Concluídas

- [x] Cadastro de Trilhas de Estudo por semestre.
- [x] Adição de tópicos específicos para cada trilha.
- [x] Marcar tópicos como concluídos.
- [x] Edição e Exclusão (CRUD completo de Trilhas e Tópicos).
- [x] **Integração com BrasilAPI:** Exibição dinâmica de feriados nacionais integrados ao FullCalendar na página inicial.
- [x] Interface Responsiva e Customizada (Tema Dark Purple).

---
##  1 - Como Executar o Projeto


```bash
### 1. Clonar o repositório
git clone [https://github.com/DGodoi19/Gerenciador-de-estudos.git](https://github.com/DGodoi19/Gerenciador-de-estudos.git)
cd "Gerenciador de estudos"

### 2. Criar ambiente virtual
python -m venv venv

### 3. Ativar ambiente virtual
  No Windows:
.\venv\Scripts\activate

### 4. Instalar dependências
pip install -r requirements.txt

### 5. Rodar Migrações e Iniciar
python manage.py migrate
python manage.py runserver
Acesse em: http://127.0.0.1:8000/
```
### 2 - Qualidade do software

- **Análise Estática (Linting)**
Utilizei o Ruff para fazer o linting do código.

```bash

ruff check .

### Fazer testes automatizados

pytest
```

### Integração Contínua (CI)
Toda vez que um código é enviado para o repositório, o GitHub Actions executa automaticamente:

- **Instalação das dependências.**

- **Verificação de linting com Ruff.**

- **Execução da suíte de testes com Pytest.**

### Funcionalidades
[x] **Cadastro de Trilhas de Estudo por semestre**

[x] **Adição de tópicos específicos para cada trilha.**

[x] **Marcar tópicos como concluídos.**

[x] **Edição e Exclusão (CRUD completo).**

[x] **Interface Responsiva.**


*Desenvolvido por Daniel Godoi Alves Watrin como parte da avaliação de Bootcamp 2, curso :Ciência da Computação.*
