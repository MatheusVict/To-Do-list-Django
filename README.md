<div align="center">
<h1>To-Do-list-Django<h1>
<h2>Uma aplicação de lista de tarefas usando Django</h2>
</div>

<h3>🔙É um projeto com foco maior no back-end end para demonstrar minhas habilidades<br><br>
Possui funções como👩‍💻:</h3>

- Validação e autenticação de cadastro e login fornecidos pelo Django.
- Área administrativa gerada pelo Django.
- O usuário pode excluir, editar, criar e ver suas tasks.
- Cada usuário vê e mexe apenas nas suas tasks.
  - Quando um usuário é apagado por um adm, todos as suas tasks são apagadas juntos.
- O usuário pode pesquisar por uma task pelo seu nome.
- Possui filtro de tasks para aquelas que que já foram feitas e as que ainda estão em andamento.
- O usuário pode editar os status das tasks.
- Possui paginação e exibe apenas 3 tasks por página.
- Exibe uma dashboard que mostras a quantidade de tasks feitas nos últimos 30 dias e as que ainda não foram feitas.
- Possui uma mensagem flash que informa ao usuário ações sucedidas ou falhas.
- Possui logout.
- Nível de acesso.

<div align="center">
  <h2>Tecnologias usadas:</h2>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
</div>

<h2 align="center">Instruções</h2>

- Crie uma virtual env e a ative no mesmo diretorio
- Entre na pasta do projeto, abra o terminal e execute o comando:
```ruby
  $ python manage.py runserver
```
- Abra seu localhost na porta 8000
- Se você não estiver autenticado não pode acessar outra rota

<video src="https://user-images.githubusercontent.com/103688000/182720513-de0bd207-c436-4aef-a3a4-c27fa6e62e83.mp4"></video>

- Para criar uma conta ADM, feche o servidor usando o comando ctrl + c no terminal
- Em seguida faça o seguinte comando:
```ruby
  $ python manage.py createsuperuser
```
- Informe o nome, email, senha, confirme a senha para esse usuário ADM
- Depois inice novamente o servidor e recarregue a página e entre com a conta ADM

> OBS: A demora no carregamento das páginas se deve a gravação da tela que consumiu recursos da máquina.

```
  {
    "nome": "To Do list",
    "author": "Matheus victor",
    "framework": "Django"
  }
```
