def cari_node(self, nama, node=None):
    if node is None:
        node = self.root

    if node.nama.lower() == nama.lower():
        return node

    for child in node.children:
        hasil = self.cari_node(nama, child)

        if hasil is not None:
            return hasil

    return None


hasil = cari_node("jokowi")

if hasil:
    print("Data ditemukan!")
    print("Nama:", hasil.nama)
    print("Jabatan:", hasil.jabatan)
else:
    print("Data tidak ditemukan!")