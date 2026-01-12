
# Sniffer Tshark

Este repositorio consta de un par de scripts que permiten entre otras cosas establecer un sniffer o ponerse a la escucha mediante el uso de tshark para capturar todos los paquetes posibles de la red donde se encuentre el equipo que inicie el programa.
## Instalación

Para poder ejecutar correctamente el script se requiere instalar algunos paquetes externos de Python, todas las referencias se ubican en el archivo **requirements.txt**.

Instalar Python en caso de que no lo tenga:

[Download Python](https://www.python.org/downloads/)

Instalación de paquetes externos:

```bash
  pip install pyshark scapy
```

Aunque el programa use scapy solo se emplea para poder exportar los paquetes a un fichero .pcap
## Funcionalidades

- **Captura y lectura de paquetes**: Además de poder captar paquetes de red (indicando previamente la interfaz donde se pondrá a la escucha), también es capaz de almacenar los paquetes que le proporcionemos mendiante un archivo .pcap, pudiendo así trabajar sobre dichos paquetes.

- **Filtrado de paquetes**: El programa es capaz de realizar un filtrado de paquetes que ya hayan sido previamente leídos o que se hayan capturado anteriormente. El filtrado se puede realizar en base a un protocolo, por ejemplo, HTTP o mediante el uso de una palabra clave.

- **Exportar paquetes**: Una vez que hayamos terminado de trabajar sobre los paquetes o si necesitamos "guardar" nuestro análisis realizado hasta el momento podemos exportarlo. El programa permite la exportación de paquetes en formato pcap. 

- **Mostrar por pantalla los paquetes**: Otra funcionalidad es la posibilidad de solicitar al programa que nos muestre por la terminal todos los paquetes recolectados o filtrados hasta ese momento, permitiendo realizar un seguimiento sobre los paquetes.



## Ejemplo de uso

A continuación se muestra un ejemplo de como se ve el programa al ejecutarlo. 

En este caso mostraré como llevar a cabo la captura de los paquetes así como filtarlo mediante TLS, y guardar los resultados en un fichero nombrado **ejemplo.pcap**.

```bash
└─$ python main.py
[1] Captura de paquetes
[2] Lectura de los paquetes
[3] Filtrar paquetes por protocolo
[4] Filtrar paquetes por texto
[5] Exportar a pcap
[6] Mostrar por pantalla los detalles de cada paquete
[7] Salir
Introduce el número según la funcionalidad a realizar: 1

Dime una interfaz: eth0
[*] Captura de paquetes iniciada, para parar pulse Ctrl+C... [*]
^C[*] Cerrando la captura de los paquetes... [*]
[+] Paquetes capturados: 1025 [+]

[1] Captura de paquetes
[2] Lectura de los paquetes
[3] Filtrar paquetes por protocolo
[4] Filtrar paquetes por texto
[5] Exportar a pcap
[6] Mostrar por pantalla los detalles de cada paquete
[7] Salir
Introduce el número según la funcionalidad a realizar: 3
Dime el protocolo a filtrar en lo paquetes: TLS
[+] Paquetes filtrados por el protocolo: TLS.
Introduce el número según la funcionalidad a realizar: 5
Dime como nombrar el archivo .pcap: ejemplo.pcap
[+] Paquetes guardados en ejemplo.pcap [+]

[1] Captura de paquetes
[2] Lectura de los paquetes
[3] Filtrar paquetes por protocolo
[4] Filtrar paquetes por texto
[5] Exportar a pcap
[6] Mostrar por pantalla los detalles de cada paquete
[7] Salir
Introduce el número según la funcionalidad a realizar: 7

Saliendo del programa...
```


## Posibles excepciones durante la ejecución del programa

En este programa salta una gran cantidad de excepciones, especialmente de tipo **EOFError**.

Todas las excepciones que puedan aparecer no impiden la correcta ejecución de ambos scripts. A continuación se muestra un ejemplo de una excepción:

```bash
Task exception was never retrieved
future: <Task finished name='Task-80' coro=<BaseTsharkOutputParser.get_packets_from_stream() done, defined at /home/kali/Desktop/Python Hacking/Seccion3/3_1_sniffer_tshark/.conda/lib/python3.11/site-packages/pyshark/tshark/output_parser/base_parser.py:4> exception=EOFError()>
Traceback (most recent call last):
  File "/home/kali/Desktop/Python Hacking/Seccion3/3_1_sniffer_tshark/sniffer_tshark.py", line 24, in start_capture
    for packet in self.capture.sniff_continuously():
  File "/home/kali/Desktop/Python Hacking/Seccion3/3_1_sniffer_tshark/.conda/lib/python3.11/site-packages/pyshark/capture/capture.py", line 221, in _packets_from_tshark_sync
    packet, data = self.eventloop.run_until_complete(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/Python Hacking/Seccion3/3_1_sniffer_tshark/.conda/lib/python3.11/asyncio/base_events.py", line 641, in run_until_complete
    self.run_forever()
  File "/home/kali/Desktop/Python Hacking/Seccion3/3_1_sniffer_tshark/.conda/lib/python3.11/asyncio/base_events.py", line 608, in run_forever
    self._run_once()
  File "/home/kali/Desktop/Python Hacking/Seccion3/3_1_sniffer_tshark/.conda/lib/python3.11/asyncio/base_events.py", line 1898, in _run_once
    event_list = self._selector.select(timeout)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kali/Desktop/Python Hacking/Seccion3/3_1_sniffer_tshark/.conda/lib/python3.11/selectors.py", line 468, in select
    fd_event_list = self._selector.poll(timeout, max_ev)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/kali/Desktop/Python Hacking/Seccion3/3_1_sniffer_tshark/.conda/lib/python3.11/site-packages/pyshark/tshark/output_parser/base_parser.py", line 22, in get_packets_from_stream
    raise EOFError()
EOFError

```
## Desarrollo

El script presentado se encuentra desarrollado en **Python**.


## Disclaimer

El script fue creado únicamente por motivos educativos, principalmente para aprender a realizar scripts o programas desarrollados en Python que involucren conceptos o casos prácticos a la Ciberseguridad o al Hacking Ético.

Se ruega utilizar los programas añadidos a este repositorios para dicho fin sobre equipos aislados o virtuales para simular el entorno, en caso contrario, no nos hacemos responsables de su uso fuera de ese ámbito.

