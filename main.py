import time
def countdown_timer(saniye):
    while saniye > 0:
        print(f"Kalan süre: {saniye} saniye")
        time.sleep(1)
        saniye -= 1

    print("Zaman doldu!")

def main():
    try:
        saniye = int(input("Geri sayım süresini saniye cinsinden girin: "))
        countdown_timer(saniye)
    except ValueError:
        print("Geçersiz girdi. Lütfen geçerli bir saniye sayısı girin.")

if __name__ == "__main__":
    main()
