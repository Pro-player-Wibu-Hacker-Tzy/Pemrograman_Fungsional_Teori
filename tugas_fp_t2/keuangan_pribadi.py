import fplib


def main():
    kas = [
        {"tanggal": "2026-10-01", "keterangan": "Gaji", "kategori": "Pemasukan", "jenis": "pemasukan", "jumlah": 5000000},
        {"tanggal": "2026-10-03", "keterangan": "Belanja", "kategori": "Makanan", "jenis": "pengeluaran", "jumlah": 250000},
        {"tanggal": "2026-10-05", "keterangan": "Transport", "kategori": "Transportasi", "jenis": "pengeluaran", "jumlah": 100000},
        {"tanggal": "2026-10-07", "keterangan": "Freelance", "kategori": "Pemasukan", "jenis": "pemasukan", "jumlah": 750000},
    ]

    kas_pemasukan = fplib.filter_data(kas, lambda x: x["jenis"] == "pemasukan")
    kas_pengeluaran = fplib.filter_data(kas, lambda x: x["jenis"] == "pengeluaran")
    pemasukan = fplib.hitung_total(kas_pemasukan, "jumlah")
    pengeluaran = fplib.hitung_total(kas_pengeluaran, "jumlah")
    saldo = pemasukan - pengeluaran
    kas_terbaru = fplib.urutkan_data(kas, "tanggal", reverse=True)
    kas_per_kategori = fplib.kelompokkan_data(kas, "kategori")

    print("Pemasukan:", fplib.format_mata_uang(pemasukan))
    print("Pengeluaran:", fplib.format_mata_uang(pengeluaran))
    print("Saldo:", fplib.format_mata_uang(saldo))
    print("Riwayat terbaru:", kas_terbaru)
    print("Riwayat per kategori:", kas_per_kategori)


if __name__ == "__main__":
    main()
