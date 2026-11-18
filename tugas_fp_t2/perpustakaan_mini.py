import fplib


def main():
    katalog = [
        {"judul": "Judul Buku", "status": "Tersedia"},
        {"judul": "Clean Code", "status": "Dipinjam"},
        {"judul": "Python Dasar", "status": "Tersedia"},
    ]
    riwayat = [
        {"peminjam": "Andi", "judul": "Clean Code", "denda": 5000},
        {"peminjam": "Budi", "judul": "Algoritma", "denda": 0},
        {"peminjam": "Andi", "judul": "Database", "denda": 3000},
    ]

    buku_tersedia = fplib.filter_data(katalog, lambda x: x["status"] == "Tersedia")
    total_denda = fplib.hitung_total(riwayat, "denda")
    daftar_denda = fplib.ekstrak_kolom(riwayat, "denda")
    riwayat_per_peminjam = fplib.kelompokkan_data(riwayat, "peminjam")
    buku_dicari = fplib.cari_data(katalog, "judul", "Judul Buku")

    print("Buku tersedia:")
    for buku in buku_tersedia:
        print("-", buku["judul"])
    print("Total denda:", fplib.format_mata_uang(total_denda))
    print("Daftar denda:", daftar_denda)
    print("Riwayat per peminjam:", riwayat_per_peminjam)
    print("Buku dicari:", buku_dicari)


if __name__ == "__main__":
    main()
