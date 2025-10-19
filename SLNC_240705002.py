import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def length(self):
        return self.size

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            new_node.next = current
            self.head = new_node
            self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.size += 1

    def add_after(self, data, value):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current:
                if current.data == value:
                    new_node.next = current.next
                    current.next = new_node
                    self.size += 1
                    return
                else :
                    current = current.next

    def display(self):
        if self.is_empty():
            print("Linked list kosong.")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()

    def search_node(self, data):
        if self.is_empty():
            print("Linked list kosong. ")
        current = self.head
        while current:
            if current.data == data:
                return True
            else:
                current = current.next
            
    def delete_node(self, data):
        #jika data kosong
        if self.head.data == data:
            self.head = self. head.next
            print("Linked list is empty. Delection is failed. ")
            return
        #jika hanya ada 1 data
        if self.head.data == data:
            self.head = self.head.next
            print(f"Node with data {data} is deleted")
            return
        
        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data {data} not found.")
            return

        prev.next = current.next
        self.size -= 1
        print(f"Node with data {data} is deleted.")

    def delete_first(self):
        current = self.head
        prev = current
        if self.is_empty():
            print("Linked list is empty. Delection Filed. ")
            return
        else:
            self.head = current.next
            #mengembalikan data yang dihapus
            return prev.data
        
    def delete_last(self):
        current = self.head
        if self.is_empty():
            print("Linked list is empty. delection is failed. ")
            return
        else:
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
                #mengemmbalikan data yang dihapus
                return prev.data
            prev.next = None


    def delete_back(self):
        temp = self.head
        while temp.next.next:
            temp = temp.nexttemp.next = None
            #menge,balikan data yang dihapus
            return prev.data
        
#contoh penggunaan linked list
my_list = LinkedList()

cek = True

while cek:
     print()
     print('\n------- Menu Utama -------')
     print('1. Tambah Elemen pada Linked List')
     print('2. Tampil Elemen dalam Linked List')
     print('3. Hapus Elemen dalam Linked List')
     print('4. Jumlah Elemen dalam Linked List')
     print('--------------------------')
     print('0. Keluar')
     print()

pil = int(input('Masukkan Pilihan anda: '))
print()
   if pil == 1:
    #os.system('cls)
    temp = True
    while temp:
        print('\n---------- Pilihan Tambah Data ----------')
        print('1. Tambah Elemen di Awal Linked List (add_first)')
        print('2. Tambah Elemen di Tengah Linked List (add_after)')
        print('3. Tambah Elemen di Akhir Linked List (add_last)')
        print('--------------------------')
        print('0. Kembali ke Menu Utama')
        print()

        pilmenu = int(input('Masukkan Pilihan anda: '))
        print()
        if pilmenu == 1:
            data = int(input('Masukkan data yang ingin ditambahkan: '))
            my_list.add_first(data)
            print(f'data {data} berhasil ditambahkan di awal linked list')
        elif pilmenu == 2:
            data = int(input('Masukkan Data yang ingin ditambahkan: '))
            value = int(input('Data ingin ditambahkan setelah data apa?: '))
            my_list.add_after(data, value)
            print(f'Data {data} berhasil ditambahkan setelah {value}')
        elif pilmenu == 3:
            data = int(input('Masukkan Data yang ingin ditambahkan: '))
            my_list.add_last(data)
            print(f'Data {data} berhasil ditambahkan di akhir linked list')
    
        elif pilmenu == 0:
            temp = False
            break
   elif pil == 2:
        print("Isi Linked List")
        my_list.display()
   elif pil == 3:
        temp = True
        while temp:
            print('\n---------- Pilihan Hapus Data ----------')
            print('1. Hapus Elemen di Awal Linked List (delete_first)')
            print('2. Hapus Elemen di Tengah Linked List (delete_node)')
            print('3. Hapus Elemen di Akhir Linked List (delete_back)')
            print('--------------------------')
            print('0. Kembali ke Menu Utama')
            print()

            pilmenu = int(input("Masukkan Pilihan Anda : "))

            if pilmenu == 1:
                hapus = my_list.delete_first()
                print(f"Data {hapus} berhasil dihapus")
            elif pilmenu == 2:
                data = int(input("Masukkan Data yang ingin dihapus : "))
                my_list.delete_node(data)
                print(f"Data {data} berhasil dihapus")
            elif pilmenu == 3:
                hapus = my_list.delete_back()
                print(f"Data {hapus} berhasil dihapus")
            elif pilmenu == 0:
                temp = False
                break
            
    elif pil == 4:
        print(f"Jumlah node dalam linked list: {my_list.length()}")
    elif pil == 0:
        print("Bye... Byee...!!")
        print()
        pil = False
        break

    else:
    print('Pilihan tidak ada')