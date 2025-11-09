import requests, re, json, os, time

def headers(bear):
    return {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {bear}',
        'content-type': 'application/json',
        'origin': 'https://www.xlaxiata.co.id',
        'referer': 'https://www.xlaxiata.co.id/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

def bearer():
    try:
        header = {
            'Referer': 'https://www.xlaxiata.co.id/registrasi',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        }
        js = requests.get(
            'https://www.xlaxiata.co.id/registrasi/_next/static/chunks/pages/regbypuk/regbypukform-b0a844f3483c094b.js',
            headers=header
        ).text
        bear = re.search(r'concat\("([^"]+)"\)', js).group(1)
    except:
        bear = "VzNicHIzR24wbjEzaW8yMDI0OmJ5ZHQybzI0KiE="
    try:
        token = requests.post(
            'https://jupiter-ms-webprereg.xlaxiata.id/generate-jwt',
            headers=headers(bear)
        ).json()['encryptToken']
    except:
        token = "Ln9YN5trk3UUGHnHXoV8644+QEDWRf8qpLJ0tovzrhQVRjJKzRulyHxNIa8eos0pH7iNIePuPNOxNmY4sRnHZIPEPD7iKAX2Z8Z2qOucrAQ+h6Z98l7GQEoIrDwRTXAD7nLAyRnH9dVwzmidCPSH9dwWBE31I739FGTNKJdqB44Ieq3PIs1y1ay6eZgmNBY84QrE22qRYOzUFWX/68cCNwFoJJdf0BdZeKclWxJAasfLAHR1bnM5V8VkNiC+CZlWe08UiEGaltTDcp2hoLGsaYshcy48PIefK3WseHwQn1SvSERWWNbHO0F70RLz7V0CXOg222YN7LQdwhm2Nv1tiw=="
    return token

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    clear()
    print("="*45)
    print("XL AUTO REGISTER")
    print("Script BY Windrase")
    print("="*45)
    print("Menu")
    print("1️⃣  Registrasi Nomor Baru")
    print("2️⃣  Keluar Program")
    print("="*45)
    pilih = input("Pilih menu (1/2): ").strip()
    if pilih == "1":
        registrasi()
    elif pilih == "2":
        print("👋 Keluar program...")
        time.sleep(1)
        exit()
    else:
        print("❌ Pilihan tidak valid!")
        time.sleep(1)
        main_menu()

def registrasi():
    clear()
    print("📱 === REGISTRASI NOMOR XL ===")
    token = bearer()
    number = input("Masukkan Nomor XL (628xx): ").strip()
    nik = input("Masukkan NIK: ").strip()
    kk = input("Masukkan No KK: ").strip()

    print("\n📩 Mengirim OTP...")
    req_otp = requests.post(
        'https://jupiter-ms-webprereg.xlaxiata.id/request-otp',
        headers=headers(token),
        json={"msisdn": number}
    )

    if req_otp.status_code != 200:
        print("❌ Gagal mengirim OTP. Coba lagi.")
        input("\nTekan Enter untuk kembali ke menu...")
        return main_menu()

    print("✅ OTP berhasil dikirim ke nomor kamu.")
    otp = input("Masukkan OTP: ").strip()

    submit = requests.post(
        'https://jupiter-ms-webprereg.xlaxiata.id/submit-registration-otp-non-biometric',
        headers=headers(token),
        json={"msisdn": number, "nik": nik, "kk": kk, "otpCode": otp}
    )

    try:
        data = submit.json()
        text = json.dumps(data, indent=2, ensure_ascii=False)
    except:
        text = submit.text

    print("\n📜 HASIL:")
    if "telah terdaftar" in text.lower():
        print("⚠️ Nomor telah terdaftar sebelumnya.")
    elif "tidak bisa digunakan" in text.lower() or "invalid" in text.lower():
        print("❌ NIK tidak bisa digunakan (kemungkinan sudah penuh).")
    elif "success" in text.lower():
        print("✅ Nomor berhasil diregistrasi!")
    else:
        print("⚠️ Respon tidak diketahui:\n", text)

    input("\nTekan Enter untuk kembali ke menu...")
    main_menu()


if __name__ == "__main__":
    main_menu()
