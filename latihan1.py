# Buat Dictionary daftar kontak
# (Note) Nama sebagai key, dan nomor sebagai value
daftarKontak = {'Ari': '081267888', 'Dina': '081267888'}

# Tampilkan kontaknya Ari
print('Menampilkan Kontak Ari : ', daftarKontak['Ari'])

# Tambah kontak baru dengan nama Riko, nomor 087654544
daftarKontak['Rico'] = "087654544"
# Ubah kontak Dina dengan nomor baru 088999776
daftarKontak['Dina'] = "088999776"

# Tampilkan semua Nama
print(daftarKontak.keys())
# Tampilkan semua Nomor
print(daftarKontak.values())
# Tampilkan daftar Nama dan nomornya
print(daftarKontak.items())

# Hapus kontak Dina
del daftarKontak['Dina']
print(daftarKontak.items())


