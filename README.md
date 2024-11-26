Berikut adalah template untuk README file Anda. Sesuaikan bagian deskripsi, penggunaan, dan contoh dengan kebutuhan Anda.

---

# Himpunan

**Himpunan** adalah paket Python sederhana untuk melakukan operasi pada himpunan, seperti gabungan, irisan, selisih, komplemen, dan himpunan kuasa.

## Fitur

- Operasi himpunan standar: gabungan, irisan, selisih.
- Mendukung operasi komplemen terhadap himpunan semesta.
- Membuat himpunan kuasa (power set).
- Penambahan dan penghapusan elemen.
- Operasi himpunan menggunakan operator Python (misalnya `+` untuk gabungan, `/` untuk irisan).

## Instalasi

Anda dapat menginstal paket ini melalui TestPyPI:

```bash
pip install -i https://test.pypi.org/simple/ himpunan
```

Setelah dipublikasikan ke PyPI utama, Anda dapat menginstalnya seperti biasa:
```bash
pip install himpunan
```

## Penggunaan

Berikut adalah contoh penggunaan sederhana:

```python
from himpunan import Himpunan

# Membuat himpunan
S = Himpunan(1, 2, 3, 4, 5, 6, 7, 8, 9)
h1 = Himpunan(1, 2, 3)
h2 = Himpunan(3, 4, 5)

# Gabungan
print("Gabungan:", h1 + h2)

# Irisan
print("Irisan:", h1 / h2)

# Selisih
print("Selisih:", h1 - h2)

# Komplemen terhadap semesta
print("Komplemen:", h1.Komplemen(S))

# Himpunan kuasa
print("Himpunan kuasa:", h1.ListKuasa())
```

Output:
```
Gabungan: {1, 2, 3, 4, 5}
Irisan: {3}
Selisih: {1, 2}
Komplemen: {4, 5, 6, 7, 8, 9}
Himpunan kuasa: [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
```

## Dokumentasi

### Kelas `Himpunan`

#### **Inisialisasi**
```python
Himpunan(*elemen)
```
- **`elemen`**: Elemen yang ingin dimasukkan ke dalam himpunan. Elemen duplikat akan otomatis dihapus.

#### **Metode**
- `tambah(item)`: Menambahkan elemen ke dalam himpunan.
- `hapus(item)`: Menghapus elemen dari himpunan.
- `Komplemen(semesta)`: Mengembalikan himpunan komplemen relatif terhadap himpunan semesta.
- `ListKuasa()`: Mengembalikan daftar semua subset (himpunan kuasa).

#### **Operator**
- `+`: Gabungan (`h1 + h2`)
- `/`: Irisan (`h1 / h2`)
- `-`: Selisih (`h1 - h2`)
- `**`: Himpunan pasangan (cartesian product) (`h1 ** h2`)
- `*`: Selisih simetris (`h1 * h2`)

---
