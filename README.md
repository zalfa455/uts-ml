# 🍊 Fruit Classification: Orange vs Grapefruit

## 📌 Deskripsi Project

Project ini bertujuan untuk membangun model *machine learning* yang dapat mengklasifikasikan buah menjadi dua kategori, yaitu **orange (jeruk)** dan **grapefruit** berdasarkan fitur fisik seperti ukuran dan warna.

Dataset yang digunakan diambil dari Kaggle dan berisi beberapa atribut numerik seperti:

* diameter
* weight
* red
* green
* blue

---

## 📂 Dataset

Dataset dapat diunduh melalui link berikut:
https://www.kaggle.com/datasets/joshmcadams/oranges-vs-grapefruit

Target klasifikasi:

* `orange` → 0
* `grapefruit` → 1

---

## ⚙️ Tahapan Pengerjaan

### 1. Data Collection

Dataset diunduh dari Kaggle dan dimuat menggunakan library `pandas`.

---

### 2. Data Understanding

Melakukan eksplorasi data:

* Melihat struktur dataset
* Mengecek tipe data
* Mengetahui distribusi label

---

### 3. Data Preprocessing

Tahapan preprocessing meliputi:

* Encoding label (orange = 0, grapefruit = 1)
* Pemilihan fitur (diameter, weight, RGB)
* Pembagian data menjadi data latih dan data uji (80:20)
* Normalisasi data menggunakan `StandardScaler` (khususnya untuk SVM)

---

### 4. Modeling

Model yang digunakan dalam penelitian ini:

#### 🌳 Decision Tree

* Model berbasis pohon keputusan
* Mudah dipahami dan diinterpretasikan

#### 📊 Naive Bayes

* Model probabilistik berbasis Teorema Bayes
* Cepat dalam proses training

#### 📈 Support Vector Machine (SVM)

* Model yang mencari hyperplane terbaik untuk memisahkan kelas
* Cocok untuk klasifikasi dengan akurasi tinggi

---

## 📊 Evaluasi Model

Evaluasi dilakukan menggunakan:

* Accuracy
* Classification Report (Precision, Recall, F1-score)

---

## 📌 Hasil Perbandingan Model

| Model         | Kelebihan         | Kekurangan                | Performa |
| ------------- | ----------------- | ------------------------- | -------- |
| Decision Tree | Mudah dipahami    | Rentan overfitting        | Baik     |
| Naive Bayes   | Cepat & sederhana | Asumsi independensi fitur | Cukup    |
| SVM           | Akurasi tinggi    | Lebih kompleks & lambat   | Terbaik  |

Berdasarkan hasil pengujian, **SVM memberikan performa terbaik** dibandingkan model lainnya.

---

## 🚀 Cara Menjalankan Program

1. Clone repository:

```
git clone https://github.com/username/uts-ml-fruit.git
```

2. Masuk ke folder project:

```
cd uts-ml-fruit
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Jalankan program:

```
python main.py
```

---

## 🧠 Kesimpulan

* Machine Learning dapat digunakan untuk klasifikasi buah berdasarkan fitur fisik.
* Dari tiga model yang diuji, **SVM menghasilkan akurasi terbaik**.
* Pemilihan model sangat berpengaruh terhadap performa klasifikasi.

---

## ✍️ Author

Nama: [Nazwa Zalfa]
NIM: [1237050031]
Mata Kuliah: Machine Learning

---
