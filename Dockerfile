# Imagem base
FROM python:3.10.2-slim

ENV TZ=America/Sao_Paulo
ENV LANG C.UTF-8
ENV LANGUAGE=pt_BR:pt
ENV LC_ALL C.UTF-8

RUN apt update && apt install -y \
        libglib2.0-0\
        libnss3\
        libnspr4\
        libatk1.0-0\
        libatk-bridge2.0-0\
        libcups2\
        libdrm2\
        libdbus-1-3\
        libxcb1\
        libxkbcommon0\
        libatspi2.0-0\
        libx11-6\
        libxcomposite1\
        libxdamage1\
        libxext6\
        libxfixes3\
        libxrandr2\
        libgbm1\
        libpango-1.0-0\
        libcairo2\
        libasound2

# Criação do diretório de trabalho
WORKDIR /home/app/


ENV PYTHONPATH=${PYTHONPATH}/home/app/src

# Instalação de dependências Python
COPY requirements.txt /home/app
RUN pip install -r requirements.txt
RUN playwright install chromium

# ENTRYPOINT ["playwright", "install", "chromium"]

CMD [ "tail", "-f", "/dev/null" ]
# CMD ["python", ""]
