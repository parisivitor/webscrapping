# Requisitos:
- Escreva um código que leia no terminal o código ICAO qualquer de um aeródromo (SBMT = campo de marte, SBJD = aeroporto de jundiaí, etc...) e imprima na tela:
- 1.As cartas disponíveis
- 2.Os horários de nascer e pôr do sol de hoje
- 3.A informação de TAF e METAR disponíveis
- Vale ressaltar que estas informações devem ser obtidas em tempo real do site, através de SCRAPPING.

# Arquitetura

O projeto foi desenvolvido seguindo os princípios de SOLID, Domain-Driven Design (DDD) e Clean Architecture. A arquitetura é dividida em camadas para facilitar a manutenção, teste e escalabilidade do sistema.

## Camadas

### Domain:
- Entidades: Nesta camada, estão as entidades principais que representam os conceitos do domínio. Por exemplo, pode haver uma entidade chamada "Aeródromo" que possui informações sobre SOL, CARAs, TAFs e METARs.
- Factory: Utilizamos o padrão de fábrica para criar instâncias de entidades de forma mais encapsulada. Por exemplo, a classe "AeródromoFactory" pode ser responsável por criar instâncias de "Aeródromo" preenchidas com informações relevantes.
- Scrap Interface: Implementamos a inversão de dependências nesta camada para evitar o acoplamento direto das entidades com bibliotecas de scraping. Isso permite que as entidades sejam independentes e facilmente testáveis.

### Application:
- Nesta camada, a implementação real do scraping é feita nos serviços. Cada serviço é responsável por executar uma operação de scraping específica no sistema.
- E a interface CLI que o usuario usará para integagir com o sistema


# Guia de Execução da Aplicação

Este guia fornece instruções passo a passo para executar a aplicação utilizando Docker e Python. Certifique-se de que o Docker esteja instalado em sua máquina antes de prosseguir.

## Passo 1: Clonar o Repositório

```bash
git clone https://github.com/parisivitor/webscrapping
cd webscrapping
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
