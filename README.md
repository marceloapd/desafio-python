# Desafio Python #Sangue-Laranja 🍊

![GitHub repo size](https://img.shields.io/github/repo-size/marceloapd/Teste-IntuitiveCare?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/marceloapd/Teste-IntuitiveCare?style=for-the-badge)

<img src="https://user-images.githubusercontent.com/71731452/191392162-0aac7698-bba3-4c01-918a-ccdcacee475e.gif" style="width:500px" alt="exemplo imagem">

> O objetivo desse desafio é avaliar o conhecimento dos candidatos. Não existe resolução certa ou errada, avaliaremos com o nível de experiência que for exigido pelas vagas disponíveis no momento. Envie o seu desafio mesmo que você não conclua todas as questões, avaliaremos tudo o que for enviado.

## Developer challenge


Sua tarefa é fazer uma aplicação que carregue a saida da URL https://jsonplaceholder.typicode.com/users , que retorna uma lista de usuário em JSON.

Faça um programa que carregue a saída dessa URL e mostre os seguintes dados:
    
- Os websites de todos os usuários

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


- O Nome, email e a empresa em que trabalha (em ordem alfabética)

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


- Mostrar todos os usuarios que contenham determinado texto no nome.

        GET /users?name=Graham
        {
            "users": [
                {
                    "id": 1,
                    "name": "Leanne Graham"
                }
            ]
        }
    

## 💻 Extras

Os problema deverão ser resolvido em uma (ou mais) das seguintes linguagens:

- Criar teste unitário para validar os itens a cima;
- Adicionar validação via Authorization Header para acessar o recurso(Pode ser um token fixo, definido em uma variavel).

## 🚀 Implementações adicionais

- Docker
- Redis
