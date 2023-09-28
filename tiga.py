def hitung_nilai_akhir(nilai_uts, nilai_uas):
    return 0.4 * nilai_uts + 0.6 * nilai_uas

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        "Mahasiswa 1": {"uts": 80, "uas": 90},
        "Mahasiswa 2": {"uts": 75, "uas": 85},
        "Mahasiswa 3": {"uts": 90, "uas": 70},
    }

    # Menghitung nilai akhir untuk semua mahasiswa dengan paradigma fungsional
    data_nilai_akhir = {nama: hitung_nilai_akhir(nilai["uts"], nilai["uas"]) for nama, nilai in data_mahasiswa.items()}

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()