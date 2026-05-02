# Wybieramy obraz bazowy z Pythonem
FROM python:3.10-slim

# Ustawiamy folder, w którym będzie żyła aplikacja w kontenerze
WORKDIR /app

# Kopiujemy wszystkie pliki z Twojego komputera do kontenera
COPY . .

# Instalujemy zależności używając Twojego polecenia z Makefile
RUN make deps

# Otwieramy port 5000 dla Flask
EXPOSE 5000

# Uruchamiamy aplikację za pomocą Makefile
CMD ["make", "run"]
