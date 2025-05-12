# 🤖 Automação de Formulário com Python e Selenium

Esse é um projetinho simples, mas bem útil, pra quem quer aprender como automatizar tarefas repetitivas usando Python. A ideia aqui é abrir um formulário HTML no navegador, preencher os campos automaticamente e enviar — tudo isso sem tocar no mouse.

---

## 📌 O que esse projeto faz?

Ele simula o que a gente normalmente faria: abrir um formulário, digitar nosso nome, e-mail, uma mensagem e clicar no botão de enviar. Mas no lugar da gente fazer isso manualmente, o Python cuida de tudo por trás com o Selenium.

---

## 🧱 Estrutura do projeto

```bash
📁 FormSelenium
├── form.html # O formulário em HTML com um toque de CSS
├── autoSelenium.py # O script que faz a mágica acontecer
└── README.md # Este arquivo aqui 😊
```

---

## 🛠 O que você precisa pra rodar

- Ter o Python instalado (recomendo a versão 3.8 ou mais recente)
- Ter o Google Chrome instalado
- Baixar o [ChromeDriver](https://chromedriver.chromium.org/) que combina com a sua versão do Chrome
- Instalar a biblioteca Selenium:

```bash
pip install selenium
```

## 🚀 Como rodar o projeto
- Baixe ou clone o projeto.

- Garanta que o chromedriver.exe esteja no mesmo lugar do script ou no PATH do sistema.

- Dá um duplo clique no autoSelenium.py ou roda ele pelo terminal assim:

```bash

python autoSelenium.py
```

O navegador vai abrir, preencher o formulário com os dados fictícios e enviar tudo sozinho.

Depois disso, ele fecha a janela automaticamente.

## 📄 Sobre o formulário
O form.html é só um formulário básico com três campos:

- Nome

- E-mail

- Mensagem

Tem também um botão de envio. Tudo bem simples, só pra praticar mesmo. Se desejar, pode personalizar à vontade — tanto os campos quanto o estilo.

## 🧠 O que dá pra aprender com isso?
- Como usar o Selenium pra automatizar coisas no navegador

- Como preencher campos com Python

- Como interagir com arquivos HTML locais

- Como pensar em pequenas automações no dia a dia


## Autor: [@Devmoises79] 👨🏾‍💻☕


