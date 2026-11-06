class Node:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.children = []
        self.parent = None


class Tree:
    def __init__(self, nama, jabatan):
        self.root = Node(nama, jabatan)

    def tambah_node(self, parent, nama, jabatan):
        node_baru = Node(nama, jabatan)
        node_baru.parent = parent
        parent.children.append(node_baru)

        print("Data berhasil ditambahkan!")
        return node_baru


org = Tree("Rektor", "Pimpinan Universitas")

dekan = org.tambah_node(
    org.root, "Dekan FST", "Dekan"
)

prodi = org.tambah_node(
    dekan, "Ketua Prodi TI", "Ketua Program Studi"
)

dosen = org.tambah_node(
    prodi, "Ahmad", "Dosen"
)