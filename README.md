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

![Featured_Image](https://user-images.githubusercontent.com/71731452/191395190-e2a83ced-fb8c-4229-b692-e16c6d9a4d7e.png)

## 🔩 Requisitos
> Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Docker
- Docker Compose

## 🧪 Testando
> Use essa collection para testar no postman

https://drive.google.com/file/d/1FbGP0p0thw71KsyhTXfxvL1wmJ57M485/view?usp=sharing
