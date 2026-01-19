[app]

# Ilova nomi (Telefonda shunday ko'rinadi)
title = Janob Amin Pro

# Paketing nomi
package.name = janobaminpro

# Paketing domeni
package.domain = org.amin

# Fayllar joylashgan joy
source.dir = .

# APK ga qo'shiladigan fayllar
source.include_exts = py,png,jpg,kv,atlas

# VERSIYA (Buni 4.0 qildik, shunda mutlaqo yangi bo'ladi!)
version = 4.0

# Kerakli kutubxonalar
requirements = python3,kivy

# Ilova belgisi (Ikonka)
# Papkangda icon.png degan rasm bo'lishi shart!
icon.filename = %(source.dir)s/icon.png

# Ekran holati (tikka)
orientation = portrait

# To'liq ekran
fullscreen = 0

# Android API darajasi
android.api = 31

# Android NDK darajasi
android.ndk = 25b

# Arxitektura (zamonaviy telefonlar uchun)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1