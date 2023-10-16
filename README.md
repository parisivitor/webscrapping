# Guia de Execução da Aplicação

Este guia fornece instruções passo a passo para executar a aplicação utilizando Docker e Python. Certifique-se de que o Docker esteja instalado em sua máquina antes de prosseguir.

## Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## Passo 2: Executar a Aplicação
Construa e inicie os contêineres Docker.
```bash
docker-compose up --build -d
```
Acesse o contêiner da aplicação.
```bash
docker exec -it qipu-scraping-app /bin/bash
```
Uma vez dentro do contêiner, execute o aplicativo Python.
```bash
python src/application/command_line_interface.py
```


## Autor:
```
Vitor Risso Parisi - Engenheiro de Software Pleno
```