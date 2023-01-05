class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self) -> bool:
        if self._size == 0:
            return True
        else:
            return False

    def printAll(self) -> None:
        if self.isEmpty() == True:
            print('Tidak ada tugas.')
        else:
            bantu = self._head
            print("=== Prioritas : Tugas ===")
            while bantu != None:
                print(f"[{bantu._priority}] : {bantu._data}")
                bantu = bantu._next

    def _addHead(self, newNode) -> None:
        baru = newNode(priority)
        if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru

    def _addTail(self, newNode) -> None:
        baru = newNode(priority)
        if self._head._priority <= priority:
                self._tail._next = baru
                baru._prev = self._tail
                self._tail = baru
                self._tail._next = None

    def _addMiddle(self, newNode) -> None:
        baru = newNode(priority)
        bantu = self._head
        while bantu._priority < priority:
            bantu = bantu._next
            bantu2 = bantu._prev
            baru._next = bantu
            bantu._prev = baru
            bantu2._next = baru
            baru._prev = bantu2

    def add(self, data, priority) -> None:
        baru = Node(data, priority)
        if self.isEmpty():
            self._head = baru
            self._tail = baru
        elif self._size == 1:
            if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            else:
                self._head._next = baru
                baru._prev = self._head
                self._tail = baru
        else:
            if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru
            elif self._head._priority <= priority:
                self._tail._next = baru
                baru._prev = self._tail
                self._tail = baru
                self._tail._next = None
            else:
                bantu = self._head
                while bantu._priority < priority:
                    bantu = bantu._next
                bantu2 = bantu._prev
                baru._next = bantu
                bantu._prev = baru
                bantu2._next = baru
                baru._prev = bantu2
        self._size += 1

    def remove(self) -> None:
        if self.isEmpty() == False:
            hapus = self._head
            if self._size == 1:
                self._head = None
            else:
                self._head = self._head._next
                self._head._prev = None
            del hapus
            self._size -= 1
        else:
            print("Sudah tidak ada tugas yang bisa dihapus.")

    def removePriority(self, priority) -> None:
        bantu = 0
        while self._data[1][bantu] != priority:
            bantu += 1
        self._data.pop(bantu)
        pass

if __name__ == "__main__":
    tugasKu = PQSTugas()
    tugasKu.add("StrukDat",1)
    tugasKu.add("Menyapu", 5)
    tugasKu.add("Cuci Baju", 4)
    tugasKu.add("Beli Alat Tulis", 3)
    tugasKu.add("Cuci Sepatu", 4)
    tugasKu.printAll()
    tugasKu.remove()
    tugasKu.printAll()
    tugasKu.removePriority(2)
    tugasKu.removePriority(4)
    tugasKu.printAll()