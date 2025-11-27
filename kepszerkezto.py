from PIL import Image
from tkinter.filedialog import askopenfilename
import tkinter as tk

def load_image():
    """Fájlböngésző ablak, ahonnan felhasználó kiválaszthat egy képet."""
    root = tk.Tk()
    root.withdraw()  # nem dob fel üres tkinter ablakot
    filename = askopenfilename(
        title="Válassz egy képet",
        filetypes=[("Képfájlok", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if filename:
        print("Kép betöltve:", filename)
        return Image.open(filename)
    else:
        print("Nem választottál ki semmit!")
        return None


def save_image(img, name_suffix):
    output_name = f"output_{name_suffix}.jpg"
    img.save(output_name)
    print(f"Kép elmentve: {output_name}")


def resize_image(img):
    w = int(input("Új szélesség: "))
    h = int(input("Új magasság: "))
    result = img.resize((w, h))
    save_image(result, "resized")


def make_bw(img):
    result = img.convert("L")
    save_image(result, "bw")


def rotate_image(img):
    angle = int(input("Hány fokkal forgassam? (90, 180, 270): "))
    result = img.rotate(angle, expand=True)
    save_image(result, f"rotated_{angle}")


def flip_image(img):
    result = img.transpose(Image.FLIP_LEFT_RIGHT)
    save_image(result, "flipped")


def menu():
    print("\n=== Képmódosító Program ===")
    print("1. Kép átméretezése")
    print("2. Fekete-fehérre alakítás")
    print("3. Elforgatás")
    print("4. Tükrözés")
    print("5. Kilépés")
    return input("Válassz egy lehetőséget: ")


def main():
    print("Kattints és válaszd ki a képet...\n")

    img = None
    while img is None:
        img = load_image()

    while True:
        choice = menu()

        if choice == "1":
            resize_image(img)
        elif choice == "2":
            make_bw(img)
        elif choice == "3":
            rotate_image(img)
        elif choice == "4":
            flip_image(img)
        elif choice == "5":
            print("Kilépés...")
            break
        else:
            print("Hibás választás!")


if __name__ == "__main__":
    main()
