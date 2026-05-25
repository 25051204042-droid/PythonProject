import time
import sys

def nyanyi_last_night_lengkap():
    HIJAU = "\033[92m"
    PUTIH = "\033[0m"
    CYAN = "\033[96m"
    KUNING = "\033[93m"

    lirik = [
        ("I texted the postcard sent to you...", 1.2, 0.08),
        ("Did it go through?", 2.2, 0.1),
        ("Sending all my love to you...", 2.5, 0.09),
        ("\nYou are the moonlight of my life", 2.0, 0.1),
        ("Every night...", 3.0, 0.12),
        ("Giving all my love to you", 2.5, 0.09),
    ]

    print(f"{HIJAU}🎸 Last Night on Earth - Green Day 🎸{PUTIH}\n")
    time.sleep(2)

    for i, (baris, jeda, speed) in enumerate(lirik):
        if "moonlight" in baris.lower():
            sys.stdout.write(KUNING)
        else:
            sys.stdout.write(CYAN)

        sys.stdout.write("    ")
        for karakter in baris:
            sys.stdout.write(karakter)
            sys.stdout.flush()

            if karakter == "?":
                time.sleep(0.5)
            elif karakter == ".":
                time.sleep(0.2)
            else:
                time.sleep(speed)

        sys.stdout.write(PUTIH)
        time.sleep(jeda)
        print()

    print(f"\n{HIJAU}--- ✨ ---{PUTIH}")


if __name__ == "__main__":
    nyanyi_last_night_lengkap()