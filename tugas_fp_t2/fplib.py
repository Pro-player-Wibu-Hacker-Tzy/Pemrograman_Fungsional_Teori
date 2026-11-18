from functools import reduce


def hitung_total(data, key):
    return reduce(lambda acc, item: acc + item[key], data, 0)


def filter_data(data, kondisi_func):
    return list(filter(kondisi_func, data))


def cari_data(data, key, value):
    return next((item for item in data if item.get(key) == value), None)


def urutkan_data(data, key, reverse=False):
    return sorted(data, key=lambda item: item[key], reverse=reverse)


def format_mata_uang(amount):
    teks = f"{amount:,.2f}"
    teks = teks.replace(",", "#").replace(".", ",").replace("#", ".")
    return f"Rp {teks}"


def hitung_persentase(part, total):
    if total == 0:
        return 0.0
    return round(part / total * 100, 2)


def ekstrak_kolom(data, key):
    return list(map(lambda item: item[key], data))


def kelompokkan_data(data, key):
    return reduce(
        lambda acc, item: {**acc, item[key]: [*acc.get(item[key], []), item]},
        data,
        {},
    )
