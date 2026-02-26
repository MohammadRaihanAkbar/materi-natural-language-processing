1. ## Tokenisasi kata dan kalimat

   Tokenisasi adalah proses memecah teks menjadi unit-unit yang lebih kecil yang disebut token. Token bisa berupa kata, frasa, atau karakter.

   Contoh: "Presiden Joko  Widodo mengunjungi Universitas Indonesia Depok di hari Senin" -> ["Presiden", "Joko", "Widodo", "mengunjungi", "Universitas", "Indonesia", "Depok", "di", "hari", "Senin"]
2. ## Normalisasi teks atau case folding

   Normalisasi teks adalah proses mengubah teks menjadi bentuk yang lebih standar atau seragam. Hal ini dilakukan untuk mengurangi variasi dalam teks yang dapat menyulitkan pemrosesan.

   Contoh: "Presiden Joko  Widodo mengunjungi Universitas Indonesia Depok di hari Senin" -> ["presiden", "joko", "widodo", "mengunjungi", "universitas", "indonesia", "depok", "di", "hari", "senin"]
3. ## Penghapusan stopword

   Stopword adalah kata-kata yang umum digunakan dalam bahasa Indonesia yang tidak memiliki makna atau arti yang signifikan. Kata-kata ini dihapus dari teks untuk mengurangi jumlah token yang akan diproses.

   Contoh: "Presiden Joko  Widodo mengunjungi Universitas Indonesia Depok di hari Senin" -> ["presiden", "joko", "widodo", "mengunjungi", "universitas", "indonesia", "depok", "senin"]
4. ## Stemming dan Lemmatization

   Stemming adalah proses mengubah kata menjadi bentuk dasarnya dengan menghapus imbuhan. Lemmatization adalah proses mengubah kata menjadi bentuk dasarnya dengan menghapus imbuhan dan mengubah kata menjadi bentuk yang benar secara tata bahasa.

   Contoh: "Presiden Joko  Widodo mengunjungi Universitas Indonesia Depok di hari Senin" -> ["presiden", "joko", "widodo", "kunjung", "universitas", "indonesia", "depok", "senin"]
