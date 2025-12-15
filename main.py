# Modules

from sniffer_tshark import SnifferTshark
import sys
# Main

if __name__ == "__main__":

    sniffer = SnifferTshark()
    packets = None
    while True:

        print("[1] Captura de paquetes")
        print("[2] Lectura de los paquetes")
        print("[3] Filtrar paquetes por protocolo")
        print("[4] Filtrar paquetes por texto")
        print("[5] Exportar a pcap")
        print("[6] Mostrar por pantalla los detalles de cada paquete")
        print("[7] Salir")

        num = input("Introduce el número según la funcionalidad a realizar: ")

        if num == "1":
            interface = input("\nDime una interfaz: ")
            sniffer.start_capture(interface)
        elif num == "2":
            pcap_file = input("Dime la ruta del fichero pcap a analizar: ")
            sniffer.read_capture(pcap_file)
        elif num == "3":
            protocol = input("Dime el protocolo a filtrar en lo paquetes: ")
            packets = sniffer.filter_by_protocol(protocol)
        elif num == "4":
            text = input("Dime el texto a filtrar: ")
            packets = sniffer.filter_by_text(text)
        elif num == "5":
            filename = input("Dime como nombrar el archivo .pcap: ")
            if packets is None:
                sniffer.export_to_pcap(packets,filename)
            else:
                sniffer.export_to_pcap(filename)
        elif num == "6":
            if packets is None:
                sniffer.print_packet_detail()
            else:
                sniffer.print_packet_detail(packets)
        elif num == "7" or "exit":
            print("Saliendo del programa...")
            sys.exit(1)
        else:
            print("Introduce un número válido [1-7]\n")