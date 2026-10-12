> Halaman ini dijana daripada README.md dan wiki/. Perubahan di sini akan ditimpa apabila wiki diterbitkan lagi.

> Halaman Bahasa Inggeris adalah yang rasmi; terjemahan ini mengikutinya.

[English](Home) | [Dansk](Home.da) | Bahasa Melayu

# Permainan Ular (hari 21)

Permainan Ular (Snake) klasik, dibina secara berorientasikan objek dengan modul `turtle` Python. Ia ialah tugasan hari ke-21 dalam *100 Days of Code: The Complete Python Pro Bootcamp* di Udemy: seekor ular bergerak sendiri merentasi skrin hitam 600 kali 600 dan dikawal dengan kekunci anak panah; ia makan makanan, membesar, dan skor dipaparkan di bahagian atas. Permainan tamat apabila kepala melepasi dinding atau menyentuh ekornya sendiri.

![Permainan pada skor 5: seekor ular hijau muda dengan kepala hijau tua dan mulut, makanan biru dan skor di bahagian atas](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/raw/branch/main/docs/images/snake-score-5.png)

*Permainan yang sedang berjalan pada skor 5: badan hijau muda, kepala hijau tua dengan mulut, makanan biru dan skor putih.*

## Kawalan

| Kekunci | Kesan |
| --- | --- |
| Atas, Bawah, Kiri, Kanan | Memusingkan ular |

Ular tidak pernah berpusing terus ke belakang ke atas dirinya sendiri. Apabila kepala menghampiri makanan biru dalam jarak kurang daripada 15 piksel, ular memakannya, bertambah panjang satu segmen dan skor naik 1.

## Jalankan

Python 3.13 atau lebih baharu dengan `tkinter` diperlukan; permainan ini tiada kebergantungan lain semasa dijalankan.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game.git
cd 021-snake-game
python -m pip install -e .
python -m snake_game
```

README repositori mempunyai persediaan penuh untuk Windows, Linux dan macOS.
