import fplib


def main():
    data_absen = [
        {"nim": "202310370110353", "nama": "Andi", "pertemuan": "Pertemuan 1", "status": "Hadir"},
        {"nim": "202310370110354", "nama": "Budi", "pertemuan": "Pertemuan 1", "status": "Alpa"},
        {"nim": "202310370110353", "nama": "Andi", "pertemuan": "Pertemuan 2", "status": "Hadir"},
        {"nim": "202310370110355", "nama": "Citra", "pertemuan": "Pertemuan 2", "status": "Izin"},
    ]

    daftar_hadir = fplib.filter_data(data_absen, lambda x: x["status"] == "Hadir")
    mahasiswa = fplib.cari_data(data_absen, "nim", "202310370110353")
    rekap_pertemuan = fplib.kelompokkan_data(data_absen, "pertemuan")
    daftar_nama = fplib.ekstrak_kolom(data_absen, "nama")
    persentase_hadir = fplib.hitung_persentase(len(daftar_hadir), len(data_absen))

    print("Mahasiswa hadir:")
    for item in daftar_hadir:
        print(f"- {item['nama']} ({item['nim']}), {item['pertemuan']}")
    print("\nMahasiswa dicari:", mahasiswa)
    print("Rekap per pertemuan:", rekap_pertemuan)
    print("Daftar nama:", daftar_nama)
    print(f"Persentase kehadiran: {persentase_hadir}%")


if __name__ == "__main__":
    main()
