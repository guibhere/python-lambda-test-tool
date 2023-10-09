# Python Lambda Test Tool

Aplicação para facilitar os testes e debugging de aplicações AWS Lambda em Python.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

List the key features and functionalities of your application:

- Feature 1: Description.
- Feature 2: Description.
- ...

## Installation

Instalar dependencias `[requirements.txt](requirements.txt)`:

```bash
pip install -r requirements.txt
```

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Lambda Test Tool UI",
            "type": "python",
            "request": "launch",
            "program": "E:/Projetos/python-lambda-test-tool/lambda_test_tool_main.py",//Path da classe principal da ferramenta de testes 
            "console": "integratedTerminal",
            "justMyCode": true,
            "args": [
                "${workspaceFolder}/serverless-api/src/app.py",//Path da classe entrypoint da aplicação lambda
                "lambda_handler",//Nome do metódo handler da lambda
                "E:/Projetos/python-serverless-api/serverless-api/events",//Path do diretorio onde se encontros os payloads json para teste
                "${workspaceFolder}/serverless-api/src/",//Path do diretorio onde se encontra a raiz do projeto
                "debug"//Argumento opcional para "pular" a tela
            ]
        }
    ]
}
```