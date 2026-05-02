# Używamy lekkiej wersji Pythona
FROM python:3.10-slim

# Instalujemy narzędzie 'make' (konieczne do wykonania RUN make deps)
RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki
COPY . .

# Teraz 'make' już zadziała
RUN make deps

# Port aplikacji
EXPOSE 5000

# Start aplikacji
CMD ["make", "run"]
