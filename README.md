# Gerenciador de Estudos Acadêmicos

*Versão:* 1.0.0  **Autor:** Daniel Godoi Alves Watrin
*Link do repositório:* https://github.com/DGodoi19/Gerenciador-de-estudos.git
*Status:* Concluído 
---

## Descrição:

Problema: Muitos alunos, sejam universitários como estudantes do ensino médio se encontram peridos hoje em dia quando o assunto é organizar melhor seus estudos, acompanhar seu progresso, gerenciar os tópicos e trilhas que o aluno está ou não aprendendo, para isso foi criado o Gerenciador de Estudos Acadêmicos. 

Aplicação web desenvolvida em Django para organização e gerenciamento de tópicos de estudo e trilhas de aprendizagem. O projeto foca em auxiliar um estudante a gerenciar seus estudos, o que está aprendendo agora, e acompanhar seu progresso de uma maneira interativa, intuitiva, e com um visual atrativo e moderno.

## Tecnologias Utilizadas

- **Framework:** [Django 4.2]
- **Linguagem:** [Python 3.12]
- **Estilização:** CSS3 personalizado (Tema Dark Purple)
- **Qualidade de Código:** [Ruff] (Linting e Análise Estática)
- **Testes:** [Pytest] com `pytest-django`
- **CI/CD:** [GitHub Actions]

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
