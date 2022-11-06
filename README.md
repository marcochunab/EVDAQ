# EVDAQ

Se describe el proceso de diseño, selección de componentes y
construcción de un sistema de adquisición de datos (DAQ) de bajo costo y de prestaciones
comparables a sistemas comerciales, a partir del uso de un micro ordenador
Raspberry PI 3b+, que permite la obtención de parámetros de voltaje, corriente y
potencia eléctrica generados por la batería de un vehículo equipado con un motor
eléctrico. La información obtenida se utiliza para determinar el rendimiento de un
vehículo eléctrico.
El procedimiento incluyó la integración de los componentes del sistema, la con-
guración del software del sistema y el desarrollo del software de adquisición de datos.
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

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Da un ejemplo
```

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Dí cómo será ese paso_

```
Da un ejemplo
```

_Y repite_

```
hasta finalizar
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0xf253fc233333078436d111175e5a76a649890000`
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
