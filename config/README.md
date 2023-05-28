# Config

Tramite questo modulo siamo in grado di prendere un sorgente e caricarlo in via seriale(collegati alla USB).
Di seguito i comandi per configurare gli esp (a partire da /config come current directory).

## Credenziali rete
Dai file `esp32.cpp` e `esp8266.cpp` si possono impostare le credenziali della rete wifi che al momento sono di esempio della rete di prova

- **ESP32**
```bash
    (ares_env) Ares/config/$ cp esp32.cpp src/main.cpp
    (ares_env) Ares/config/$ platformio run -e esp32 -t upload
```

- **ESP8266**
```bash
    (ares_env) Ares/config/$ cp esp8266.cpp src/main.cpp
    (ares_env) Ares/config/$ platformio run -e esp8266 -t upload
```

## Indirizzo IP
Per conoscere l'indirizzo IP del dispositivo possiamo aggiungere `-t upload` al secondo comando.
In alternativa possiamo aprire il monitor seriale con il comando
```bash
    (ares_env) ./$ platformio run -t monitor
```