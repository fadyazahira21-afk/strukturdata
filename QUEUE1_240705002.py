class Queue:
    def __init__(self):
        self.qlist = list()

    def isEmpty(self):
        return len(self.qlist) == 0
    
    def __len__(self):
        return len(self.qlist)
    
    def enqueue(self,data):
        self.qlist.append(data)

    def dequeue(self):
        if self.isEmpty():
           print('Queue kosong. Tidak ada data yang dapat dequeue')
        else:
            return self.qlist.pop(0)

    def display(self):
        if self.isEmpty():
            print('Queue kosong. Tidak ada data yang dapat ditampilkan')
        else:
            for item in self.qlist:
                print(item, end=' ')
            print()


    def deleteAll(self):
        while not self.isEmpty():
            self.dequeue()

# Create Queue
myQueue = Queue()

cek = True

while cek:
    print()
    print('--------Masukkaan Pilihan Anda-------')
    print(' 1. Tambah elemen pada queue')
    print(' 2. Tampil elemen pada queue')
    print(' 3. Hapus elemen dalam queue')
    print(' 4. Hapus seluruh data dalam queue')
    print('--------------------------------------')
    print(' 0. Keluar')
    print()

    pil = int(input('Masukkan Pilihan Anda: '))

    if pil == 1:
        jum = int(input('Masukkan jumlah data yang ingin diinputkan: '))
        if jum > 0:
            i = 1
            while i <= jum:
                data = input('Masukkan data yang ingin diinput: ')
                myQueue.enqueue(data)
                i+=1
        else:
            print('Jumlah data minimal 1 !!')
           
    elif pil == 2:
        print("Isi Queue: ")
        myQueue.display()
    elif pil == 3:
        myQueue.dequeue()
        print('Data telah dihapus')
    elif pil == 4:
        myQueue.deleteAll()
        print('Seluruh data telah dihapus')
    elif pil == 0:
        print("Bye troopers...\n")
        pil = False
        break
    else:
        print('Pilihsn tidak ada')


