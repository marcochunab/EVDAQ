# EVDAQ

Se describe el proceso de diseño, selección de componentes y
construcción de un sistema de adquisición de datos (DAQ) de bajo costo y de prestaciones
comparables a sistemas comerciales, a partir del uso de un micro ordenador
Raspberry PI 3b+, que permite la obtención de parámetros de voltaje, corriente y
potencia eléctrica generados por la batería de un vehículo equipado con un motor
eléctrico. La información obtenida se utiliza para determinar el rendimiento de un
vehículo eléctrico.
El procedimiento incluyó la integración de los componentes del sistema, la configuración 
del software del sistema y el desarrollo del software de adquisición de datos.
El sistema prototipo se probó en condiciones de laboratorio, utilizando un dinamó-
metro de chasis para la evaluación de consumo energético para cumplir un ciclo de
conducción NEDC (New European Driving Cycle).
La información obtenida por el sistema desarrollado se comparó con mediciones
tomadas por un sistema de adquisición de datos comercial Sirius Dewesoft XHS,
teniendo un error en medición menor al 1 %.

## Componentes Seleccionados

El ordenador seleccionado fue Raspberry PI 3B+, permite la creación de un sistema
de cómputo embebido debido a su micro procesador, con la capacidad de adquirir
señales sin necesidad de alguna tarjeta DAQ adicional y procesar los datos para las
pruebas de obtención de corriente, voltaje y potencia eléctrica de un vehículo eléctrico,
es un sistema económico y de fácil acceso, una desventaja es que no tiene entradas
analógicas pero se resuelve con un módulo externo.
Raspberry PI cuenta con la opción de utilizar un sistema operativo Raspbian, el
cual permite realizar multitareas como un ordenador convencional y para la creación
de la aplicación de control emplea lenguaje de programación Phyton con una variedad
de opciones disponibles en librerías. La placa tiene un procesador potente que
trabaja a 1.4 Ghz, y además elimina el cuello de botella de la conectividad incluyendo
Bluetooth 4.2, BLE, Wi-Fi a doble banda 2.4 Ghz y 5 Ghz y, además, la tarjeta de
red, Gigabit Ethernet, es capaz de alcanzar los 300 Mbps al funcionar sobre USB 2.0 1.

La placa cuenta con cuatro puertos USB 2.0, el puerto RJ45 para conexiones
Ethernet, la toma de auriculares, el conector HDMI, el puerto MicroUSB para la
alimentación o el ya clásico puerto GPIO.
A continuación, se detalla todas las características del modelo:
- CPU + GPU: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @1.4GHz.
- RAM: 1GB LPDDR2 SDRAM.
- Wi-Fi + Bluetooth: 2.4GHz y 5GHz IEEE 802.11.b/g/n/ac, Bluetooth 4.2, BLE.
- Ethernet: Gigabit Ethernet sobre USB 2.0 (300 Mbps).
- GPIO de 40 pines.
- HDMI.
- 4 puertos USB 2.0.
- Puerto CSI para conectar una cámara.
- Puerto DSI para conectar una pantalla táctil.
- Salida de audio estéreo y vídeo compuesto.
- Micro-SD.
- Power-over-Ethernet (PoE).
## 
