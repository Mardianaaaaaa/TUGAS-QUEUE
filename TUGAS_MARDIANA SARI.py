#Cara Kerja Antrian Printer
import queue

class PrinterQueue:
    def __init__(self):
        self.q = queue.Queue()

    def is_empty(self):
        return self.q.empty()

    def enqueue(self, item):
        self.q.put(item)

    def dequeue(self):
        if not self.is_empty():
            return self.q.get()
        else:
            return None

    def tampilkan_antrian(self):
        return list(self.q.queue)

def tampilkan_status_antrian(printer_queue):
    if not printer_queue.is_empty():
        antrian = printer_queue.tampilkan_antrian()
        print("Antrian dokumen:", antrian)
        print(f"Total dokumen dalam antrian: {len(antrian)}")
    else:
        print("Antrian kosong.")

if __name__ == "__main__":
    queue_printer = PrinterQueue()

    while True:
        print("\nMenu Printer:")
        print("[1] Tambahkan Dokumen")
        print("[2] Cetak Dokumen")
        print("[3] Lihat Antrian") 
        print("[4] Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            nama = input("Masukkan nama dokumen: ")
            queue_printer.enqueue(nama)
            print(f"Dokumen '{nama}' ditambahkan ke antrian.")
            tampilkan_status_antrian(queue_printer)

        elif pilihan == "2":
            hasil = queue_printer.dequeue()
            if hasil is not None:
                print(f"Mencetak dokumen: {hasil}")
                tampilkan_status_antrian(queue_printer)
            else:
                print("Antrian kosong, tidak ada dokumen yang dicetak.")

        elif pilihan == "3":
            print("Melihat antrian dokumen:")
            tampilkan_status_antrian(queue_printer)

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

