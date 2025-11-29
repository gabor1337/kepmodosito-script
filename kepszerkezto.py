import os
from PIL import Image
from tkinter.filedialog import askdirectory
import tkinter as tk


def choose_folder():
    root = tk.Tk()
    root.withdraw()
    folder = askdirectory(title="Válassz egy mappát a képekhez")
    if folder:
        print("Képek betöltése innen:", folder)
        return folder
    else:
        print("Nem választottál mappát!")
        return None



def get_images_in_folder(folder):
    supported = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    return [f for f in os.listdir(folder) if f.lower().endswith(supported)]



def save_image(img, output_folder, original_name, suffix, ext_override=None):
    name, ext = os.path.splitext(original_name)

    if ext_override is None:
        new_ext = ".jpg"
    else:
        new_ext = ext_override

    output_path = os.path.join(output_folder, f"{name}_{suffix}{new_ext}")
    img.save(output_path)
    print("Mentve:", output_path)



def resize_image(img, w, h):
    return img.resize((w, h))


def make_bw(img):
    return img.convert("L")


def rotate_image(img, angle):
    return img.rotate(angle, expand=True)


def flip_image(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)


def convert_png_to_jpg(img):
    return img.convert("RGB")


def convert_jpg_to_png(img):
    return img


# --- Menü ---
def menu():
    print("\n=== Batch Képmódosító Program ===")
    print("1. Képek átméretezése")
    print("2. Fekete-fehérre alakítás")
    print("3. Képek elforgatása")
    print("4. Tükrözés")
    print("5. PNG → JPG átalakítás")
    print("6. JPG → PNG átalakítás")
    print("7. Kilépés")
    return input("Válassz: ")



def main():
    print("Válassz egy mappát a képekhez...\n")

    folder = None
    while folder is None:
        folder = choose_folder()

    images = get_images_in_folder(folder)
    if not images:
        print("A mappában nincsenek képek!")
        return

    output_folder = os.path.join(folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    while True:
        choice = menu()

        
        if choice == "7":
            print("Kilépés...")
            break

        
        if choice == "1":
            w = int(input("Új szélesség: "))
            h = int(input("Új magasság: "))

            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                result = resize_image(img, w, h)
                save_image(result, output_folder, file, "resized")

        
        elif choice == "2":
            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                result = make_bw(img)
                save_image(result, output_folder, file, "bw")

        
        elif choice == "3":
            angle = int(input("Hány fokkal forgassam? (90, 180, 270): "))

            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                result = rotate_image(img, angle)
                save_image(result, output_folder, file, "rotated")

       
        elif choice == "4":
            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                result = flip_image(img)
                save_image(result, output_folder, file, "flipped")

        
        elif choice == "5":
            for file in images:
                if file.lower().endswith(".png"):
                    path = os.path.join(folder, file)
                    img = Image.open(path)

                    result = convert_png_to_jpg(img)
                    save_image(result, output_folder, file, "png_to_jpg", ".jpg")
                else:
                    print(f"{file} nem PNG, kihagyva!")

       
        elif choice == "6":
            for file in images:
                if file.lower().endswith((".jpg", ".jpeg")):
                    path = os.path.join(folder, file)
                    img = Image.open(path)

                    result = convert_jpg_to_png(img)
                    save_image(result, output_folder, file, "jpg_to_png", ".png")
                else:
                    print(f"{file} nem JPG, kihagyva!")

        else:
            print("Hibás választás!")
            continue

        print("\nMinden kép feldolgozva!\n")


if __name__ == "__main__":
    main()
