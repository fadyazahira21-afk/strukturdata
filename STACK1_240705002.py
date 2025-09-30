import os
from queue import LifoQueue
from collections import deque

print()
MaxSize = int(input('Masukkan Jumlah data yang ingin ditambah: '))

DequeStack = deque()
LifoStack = LifoQueue(maxsize=MaxSize)

cek = True
while cek:
    os.system('cls')   
    print('Masukkan pilihan anda')
    print('1. Stack dengan Deque')
    print('2. Stack dengan LifoQueue')
    print('0. Keluar')

    pil = int(input('Masukkan pilihan anda: '))

    if pil == 1:
        os.system('cls')
        temp = True
        while temp:
            print()
            print('-Masukkan pilihan anda')
            print(' 1. Tambah data dengan Deque')
            print(' 2. Hapus data Deque')
            print(' 3. Tampil data Deque')
            print(' 4. Jumlah data Deque')
            print(' 0. Keluar')
            pilMenu = int(input('Masukkan pilihan anda: '))
            print()

            if pilMenu == 1:
                if len(DequeStack) < MaxSize:
                    item = input(f'Masukkan data ke-{len(DequeStack)+1}: ')
                    DequeStack.append(item)
                else:
                    print('Data tidak bisa ditambah, Stack sudah penuh!!')
            elif pilMenu == 2:
                if len(DequeStack) != 0:
                    print(f'Elemen terakhir: {DequeStack.pop()} telah dihapus')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')
            elif pilMenu == 3:
                print('Data dalam stack adalah: ')
                print(list(DequeStack))
            elif pilMenu == 4:
                print(f'Jumlah data dalam stack = {len(DequeStack)}')
            elif pilMenu == 0:
                temp = False
            else:
                print("Pilihan tidak ada")

    elif pil == 2:
        os.system('cls')
        temp = True
        while temp:
            print()
            print('-Masukkan pilihan anda')
            print(' 1. Tambah data dengan LifoQueue')
            print(' 2. Hapus data LifoQueue')
            print(' 3. Tampil data LifoQueue')
            print(' 4. Jumlah data LifoQueue')
            print(' 0. Kemluar')
            pilMenu = int(input('Masukkan pilihan anda: '))
            print()

            if pilMenu == 1:
                if not LifoStack.full():
                    item = input(f'Masukkan data ke-{LifoStack.qsize()+1}: ')
                    LifoStack.put(item)
                else:
                    print('Data tidak bisa ditambah. Stack sudah penuh!')
            elif pilMenu == 2:
                if not LifoStack.empty():
                    print(f'Elemen terakhir: {LifoStack.get()} telah dihapus')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')
            elif pilMenu == 3:
                isi = list(LifoStack.queue)
                print('Data dalam stack adalah: ')
                print(isi)
            elif pilMenu == 4:
                print(f'Jumlah data dalam Stack = {LifoStack.qsize()}')
            elif pilMenu == 0:
                temp = False
            else:
                print("Pilihan tidak ada")

    elif pil == 0:
        cek = False
        print("Program selesai.")
    else:
        print('Pilihan tidak ada')
