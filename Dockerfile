FROM debian:10

RUN apt get-install --no-cache python3-dev 
    && pip3 install --upgrade pip

WORKDIR /desafioMeli

COPY . /desafioMeli

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "desafio/app.py"]