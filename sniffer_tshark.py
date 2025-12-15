import pyshark
from scapy.all import wrpcap,Ether
class SnifferTshark:
    
    def __init__(self):
        self.capture = None
        self.captured_packets = []

    def start_capture(self,interface="all",display_filter=""):
        """
        Realiza la captura de paquetes en tiempo real hasta teclear Ctrl+C.
            Args:
                interface(str): Indica la interfaz a analizar en tiempo real.
                display_filter(str): En caso necesario, emplear un filtro.
        """

        try:
            self.capture = pyshark.LiveCapture(interface=interface,display_filter=display_filter,
                                           use_json = True,
                                           include_raw=True
                                           )
            
            print("[*] Captura de paquetes iniciada, para parar pulse Ctrl+C... [*]")
            for packet in self.capture.sniff_continuously():
                self.captured_packets.append(packet)

        except (KeyboardInterrupt, EOFError):
            print("[*] Cerrando la captura de los paquetes... [*]")
            print(f"[+] Paquetes capturados: {len(self.captured_packets)} [+]\n")

    def read_capture(self, pcap_file, display_filter=""):
        """
        A partir de un fichero proporcionado, el programa se encarga de leer los paquetes.
            Args:
                pcap_file(str): Ruta del fichero que se quiera leer.
                display_filter(str): En caso necesario, emplear un filtro.
        """

        try:
            self.capture = pyshark.FileCapture(
                input_file=pcap_file,
                display_filter=display_filter,
                keep_packets=False, # <- No mantiene los paquetes en memoria RAM para que no se pete
                use_json=True,
                include_raw=True

            )

            self.captured_packets = [pkt for pkt in self.capture]
            print(f"[+] Lectura de {pcap_file} realizada correctamente.[+]\n")

        except Exception:
            print(f"[-] Error al leer el archivo {pcap_file} [-]")

    def filter_by_protocol(self,protocol):
        filtered_packets = [pkt for pkt in self.captured_packets if protocol in pkt]
        if filtered_packets:
            print(f"[+] Paquetes filtrados por el protocolo: {protocol}.")
        else:
            print(f"[-] No se ha filtrado los paquetes correctamente.")
        return filtered_packets
    
    def filter_by_text(self,text):
        filtered_packets = []
        for pkt in self.captured_packets:
            for layer in pkt.layers:
                for field_line in layer._get_all_field_lines(): # <- Saca cada una de las líneas de los campos que componen cada uno de los layers
                    if text in field_line:
                        filtered_packets.append(pkt)
        if filtered_packets:
            print(f"[+] Paquetes filtrados por el protocolo: {text}.")
        else:
            print(f"[-] No se ha filtrado los paquetes correctamente.")
        return filtered_packets
    
    def export_to_pcap(self, packets = None, filename="capture.pcap"):
        packets = self.captured_packets
        scapy_packets = [Ether((pkt.get_raw_packet())) for pkt in packets]
        wrpcap(filename, scapy_packets)
        print(f"[+] Paquetes guardados en {filename} [+]\n")

    def print_packet_detail(self, packets = None):
        if packets is None:
            packets = self.captured_packets
        
        for packet in packets:
            if packet == packets[0]:
                print("[*] Imprimiendo los paquetes [*]\n")
            print(packet)
            print("-----")