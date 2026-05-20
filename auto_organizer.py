import os
import shutil

papkalar = {
    "Rasmlar": [".jpg", ".jpeg", ".png", ".gif"],
    "Hujjatlar": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videolar": [".mp4", ".mkv", ".avi"],
    "Dasturlar": [".exe", ".msi", ".zip", ".rar"]
}

yo'l = input("📁 Tartiblamoqchi bo'lgan papka yo'lini kiriting: ")
if os.path.exists(yo'l):
    for fayl in os.listdir(yo'l):
        fayl_yo'li = os.path.join(yo'l, fayl)
        if os.path.isfile(fayl_yo'li):
            kengaytma = os.path.splitext(fayl)[1].lower()
            joylandi = False
            for papka_nomi, formatlar in papkalar.items():
                if kengaytma in formatlar:
                    yangi_papka = os.path.join(yo'l, papka_nomi)
                    os.makedirs(yangi_papka, exist_ok=True)
                    shutil.move(fayl_yo'li, yangi_papka)
                    print(f"🚚 {fayl} -> {papka_nomi} papkasiga ko'chirildi")
                    joylandi = True
                    break
    print("✅ Tartiblash yakunlandi!")