# Desafio Python

![GitHub repo size](https://img.shields.io/github/repo-size/marceloapd/desafio-python?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/marceloapd/desafio-python?style=for-the-badge)

<img src="https://user-images.githubusercontent.com/71731452/191392162-0aac7698-bba3-4c01-918a-ccdcacee475e.gif" style="width:500px" alt="exemplo imagem">

> O objetivo desse desafio é avaliar o conhecimento dos candidatos. Não existe resolução certa ou errada, avaliaremos com o nível de experiência que for exigido pelas vagas disponíveis no momento. Envie o seu desafio mesmo que você não conclua todas as questões, avaliaremos tudo o que for enviado.

## Developer challenge


Sua tarefa é fazer uma aplicação que carregue a saida da URL https://jsonplaceholder.typicode.com/users , que retorna uma lista de usuário em JSON.

Faça um programa que carregue a saída dessa URL e mostre os seguintes dados:

<details>
<summary>Os websites de todos os usuários</summary>
<pre>
        GET /users/websites
        {
            "websites": [
                {
                    "website": "hildegard.org"
                },
                ...
                {
                    "website": "ambrose.net"
                }
            ]
        }

</pre>
</details>    

<details>
<summary>O Nome, email e a empresa em que trabalha (em ordem alfabética)</summary>
<pre>
        GET /users/detail
        {
            "users": [
                {
                    "name": "Chelsey Dietrich",
                    "email": "Lucio_Hettinger@annie.ca",
                    "company": "Keebler LLC"
                },
                ...
                {
                    "name": "Patricia Lebsack",
                    "email": "Julianne.OConner@kory.org",
                    "company": "Robel-Corkery"
                }
            ]
        }

</pre>
</details>  

<details>
<summary>Mostrar todos os usuarios que contenham determinado texto no nome</summary>
<pre>
        GET /users?name=Graham
        {
            "users": [
                {
                    "id": 1,
                    "name": "Leanne Graham"
                }
            ]
        }

</pre>
</details>  

## 💻 Extras

- Criar teste unitário para validar os itens a cima;
- Adicionar validação via Authorization Header para acessar o recurso(Pode ser um token fixo, definido em uma variavel).

## 🚀 Implementações adicionais

- Docker
- Redis

## 👷 Arquitetura

<img src="https://user-images.githubusercontent.com/71731452/192170155-9162b7b5-af8a-44b0-9580-ab35a74c1dd8.png" style="width:400px" alt="Arquitetura Geral">

## 🔩 Requisitos
> Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Docker
- Docker Compose

## ⚙️ Configuração
> Na pasta raiz, faça uma cópia do env-sample e renomeie-o para .env

```
cp env-sample .env
```
## 🏃 Rodando
> Você só precisa executar os contêineres com o docker compose

```
docker compose up --build
```

## 🧪 Testando
> Use essa collection para testar no postman

Collection link: https://www.getpostman.com/collections/7fcf093536f18a03685d
