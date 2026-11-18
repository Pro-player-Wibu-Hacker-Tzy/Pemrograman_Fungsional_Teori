import fplib


def main():
    menu = [
        {"nama": "Nasi Goreng", "harga": 15000, "stok": 10},
        {"nama": "Mie Goreng", "harga": 12000, "stok": 8},
        {"nama": "Es Teh", "harga": 5000, "stok": 20},
        {"nama": "Sup Ayam", "harga": 10000, "stok": 0},
    ]
    keranjang = [
        {"nama": "Nasi Goreng", "harga": 15000},
        {"nama": "Es Teh", "harga": 5000},
    ]

    menu_aktif = fplib.filter_data(menu, lambda x: x["stok"] > 0)
    menu_termurah = fplib.urutkan_data(menu, "harga")
    nama_menu = fplib.ekstrak_kolom(menu, "nama")
    total = fplib.hitung_total(keranjang, "harga")
    harga_nasi = fplib.hitung_total(
        fplib.filter_data(keranjang, lambda item: item["nama"] == "Nasi Goreng"),
        "harga",
    )
    persentase_nasi = fplib.hitung_persentase(harga_nasi, total)

    print("Menu aktif:")
    for item in menu_aktif:
        print(f"- {item['nama']}: {fplib.format_mata_uang(item['harga'])}")
    print("\nMenu termurah ke termahal:")
    for item in menu_termurah:
        print(f"- {item['nama']}: {fplib.format_mata_uang(item['harga'])}")
    print("\nDaftar nama menu:", nama_menu)
    print("Total belanja:", fplib.format_mata_uang(total))
    print(f"Persentase Nasi Goreng: {persentase_nasi}%")


if __name__ == "__main__":
    main()
