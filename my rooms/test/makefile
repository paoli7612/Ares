.PHONY: all clean esp32 esp8266

clean:
	rm -rf src log

esp32: clean
	mkdir -p src log
	cp esp32.cpp src/main.cpp
	platformio run -e esp32-1 --target upload && echo 'ok' > log/esp32-1.txt
	platformio run -e esp32-2 --target upload && echo 'ok' > log/esp32-2.txt
	platformio run -e esp32-3 --target upload && echo 'ok' > log/esp32-3.txt

esp8266: clean
	mkdir -p src log
	cp esp8266.cpp src/main.cpp
	platformio run -e esp8266-1 --target upload && echo 'ok' > log/esp8266-1.txt
	platformio run -e esp8266-2 --target upload && echo 'ok' > log/esp8266-2.txt
	platformio run -e esp8266-3 --target upload && echo 'ok' > log/esp8266-3.txt

esp32led: clean
	mkdir -p src log
	cp esp32led.cpp src/main.cpp
	platformio run -e esp32-1 --target upload && echo 'ok' > log/esp32-1.txt
	platformio run -e esp32-2 --target upload && echo 'ok' > log/esp32-2.txt
	platformio run -e esp32-3 --target upload && echo 'ok' > log/esp32-3.txt

esp8266led: clean
	mkdir -p src log
	cp esp8266led.cpp src/main.cpp
	platformio run -e esp8266-1 --target upload && echo 'ok' > log/esp8266-1.txt
	platformio run -e esp8266-2 --target upload && echo 'ok' > log/esp8266-2.txt
	platformio run -e esp8266-3 --target upload && echo 'ok' > log/esp8266-3.txt
