from copy import deepcopy
import fplib


DATA = [{"nama": "Teh", "harga": 3000}, {"nama": "Roti", "harga": 5000}]


def test_hitung_total_akurat():
    assert fplib.hitung_total(DATA, "harga") == 8000


def test_hitung_total_list_kosong():
    assert fplib.hitung_total([], "harga") == 0


def test_hitung_total_tidak_mutasi():
    salinan = deepcopy(DATA)
    fplib.hitung_total(DATA, "harga")
    assert DATA == salinan


def test_filter_data_akurat():
    assert fplib.filter_data(DATA, lambda x: x["harga"] >= 5000) == [DATA[1]]


def test_filter_data_list_kosong():
    assert fplib.filter_data([], lambda x: True) == []


def test_filter_data_tidak_mutasi():
    salinan = deepcopy(DATA)
    fplib.filter_data(DATA, lambda x: x["harga"] > 0)
    assert DATA == salinan


def test_cari_data_akurat():
    assert fplib.cari_data(DATA, "nama", "Teh") == DATA[0]


def test_cari_data_tidak_ditemukan_dan_list_kosong():
    assert fplib.cari_data(DATA, "nama", "Kopi") is None
    assert fplib.cari_data([], "nama", "Teh") is None


def test_cari_data_tidak_mutasi():
    salinan = deepcopy(DATA)
    fplib.cari_data(DATA, "nama", "Teh")
    assert DATA == salinan


def test_urutkan_data_akurat():
    assert fplib.urutkan_data(DATA, "harga", reverse=True)[0]["nama"] == "Roti"


def test_urutkan_data_list_kosong():
    assert fplib.urutkan_data([], "harga") == []


def test_urutkan_data_tidak_mutasi():
    salinan = deepcopy(DATA)
    fplib.urutkan_data(DATA, "harga")
    assert DATA == salinan


def test_format_mata_uang_akurat():
    assert fplib.format_mata_uang(10000) == "Rp 10.000,00"


def test_format_mata_uang_nol():
    assert fplib.format_mata_uang(0) == "Rp 0,00"


def test_format_mata_uang_tidak_mutasi():
    salinan = deepcopy(DATA)
    fplib.format_mata_uang(10000)
    assert DATA == salinan


def test_hitung_persentase_akurat():
    assert fplib.hitung_persentase(3, 4) == 75.0


def test_hitung_persentase_total_nol():
    assert fplib.hitung_persentase(5, 0) == 0.0


def test_hitung_persentase_tidak_mutasi():
    salinan = deepcopy(DATA)
    fplib.hitung_persentase(3, 4)
    assert DATA == salinan


def test_ekstrak_kolom_akurat():
    assert fplib.ekstrak_kolom(DATA, "nama") == ["Teh", "Roti"]


def test_ekstrak_kolom_list_kosong():
    assert fplib.ekstrak_kolom([], "nama") == []


def test_ekstrak_kolom_tidak_mutasi():
    salinan = deepcopy(DATA)
    fplib.ekstrak_kolom(DATA, "nama")
    assert DATA == salinan


def test_kelompokkan_data_akurat():
    data = [{"k": "A", "v": 1}, {"k": "A", "v": 2}, {"k": "B", "v": 3}]
    assert fplib.kelompokkan_data(data, "k") == {
        "A": [data[0], data[1]],
        "B": [data[2]],
    }


def test_kelompokkan_data_list_kosong():
    assert fplib.kelompokkan_data([], "k") == {}


def test_kelompokkan_data_tidak_mutasi():
    salinan = deepcopy(DATA)
    fplib.kelompokkan_data(DATA, "nama")
    assert DATA == salinan
