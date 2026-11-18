import fplib


def main():
    daftar_nilai = [
        {"nim": "202310370110353", "nama": "Andi", "nilai_akhir": 85},
        {"nim": "202310370110354", "nama": "Budi", "nilai_akhir": 55},
        {"nim": "202310370110355", "nama": "Citra", "nilai_akhir": 70},
    ]
    komponen_nilai = [
        {"komponen": "UTS", "skor": 80, "bobot": 40, "nilai_berbobot": 32},
        {"komponen": "UAS", "skor": 90, "bobot": 60, "nilai_berbobot": 54},
    ]

    total_skor = fplib.hitung_total(komponen_nilai, "skor")
    total_nilai_berbobot = fplib.hitung_total(komponen_nilai, "nilai_berbobot")
    ranking = fplib.urutkan_data(daftar_nilai, "nilai_akhir", reverse=True)
    mahasiswa_lulus = fplib.filter_data(daftar_nilai, lambda x: x["nilai_akhir"] >= 60)
    mahasiswa_dicari = fplib.cari_data(daftar_nilai, "nim", "202310370110353")
    persentase_lulus = fplib.hitung_persentase(len(mahasiswa_lulus), len(daftar_nilai))

    print("Total skor komponen:", total_skor)
    print("Nilai akhir berbobot:", total_nilai_berbobot)
    print("Peringkat:", ranking)
    print("Mahasiswa lulus:", mahasiswa_lulus)
    print("Mahasiswa dicari:", mahasiswa_dicari)
    print(f"Persentase kelulusan: {persentase_lulus}%")


if __name__ == "__main__":
    main()
