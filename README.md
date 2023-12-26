# Front-end para a API xinga.me

Este projeto consiste em um front-end simples para a API xinga.me (https://github.com/leozz37/profanity). Abaixo, você encontrará as instruções para configurar e executar o projeto em sua máquina.

## Pré-requisitos

- Certifique-se de ter o Python instalado em sua máquina. Você pode fazer o download em [python.org](https://www.python.org/downloads/).

## Configuração do Ambiente

1. Clone este repositório em sua máquina usando o seguinte comando no terminal:

   ```bash
   git clone https://github.com/jeressy/Gerador-de-Desaforo.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd Gerador-de-Desaforo
   ```

3. Crie um ambiente virtual para o projeto. Execute os seguintes comandos:

   ```bash
   python -m venv venv
   ```

   - No Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - No Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Executando o Projeto

1. Com o ambiente virtual ativado, execute o seguinte comando para iniciar o servidor Flask:

   ```bash
   python app.py
   ```

2. Abra seu navegador e acesse [http://localhost:5000](http://localhost:5000).

Agora você deverá ver a aplicação em execução localmente. Sinta-se à vontade para explorar e gerar xingamentos de forma recreativa.

## Observação

Este projeto utiliza a biblioteca `requests` para fazer chamadas à API xinga.me. Certifique-se de ter conexão com a internet ao executar o projeto.

---

Espero que essas instruções ajudem você a configurar e executar o projeto em sua máquina! Se houver algum problema ou dúvida, sinta-se à vontade para abrir uma issue no [repositório do projeto](https://github.com/jeressy/Gerador-de-Desaforo).
