Atividade: Cookies e Sessões com Flask
 


1. Identificação por Cookie:
Crie uma rota /nome/<nome> que salva o nome do usuário em um cookie. Na página inicial, exiba uma saudação personalizada como utilizando o valor armazenado no cookie. Caso o cookie não exista, exiba .



2. Contador de Visitas:
Implemente um contador que registra quantas vezes o usuário acessou a página inicial. O contador deve ser armazenado em um cookie e incrementado a cada visita. Exiba na página a mensagem .



3. Login com Sessão:
Crie um sistema de login simples com as seguintes rotas:
GET /login — exibe um formulário com campos de usuário e senha
POST /login — valida as credenciais e inicia uma sessão
GET /perfil — exibe os dados do usuário logado (protegida — redireciona para /login se não houver sessão ativa)
GET /logout — encerra a sessão e redireciona para /login



4. Expiração de Cookie: Delete o Cookie através da ferramenta de desenvolvimento do Browser (ex: Inspect do Google Chrome) Application/Cookies e veja se o contador foi zerado, bem como o nome do visitante.
