import os
from PIL import Image
from tkinter.filedialog import askdirectory
import tkinter as tk

# Mappa kiválasztása
def choose_folder():
    root = tk.Tk()
    root.withdraw()
    folder = askdirectory(title="Válassz egy mappát a képekhez")
    if folder:
        print("Képek betöltve innen:", folder)
        return folder
    else:
        print("Nem választottál!")
        return None


# Képek listázása 
def get_images_in_folder(folder):
    supported = (".jpg", ".jpeg", ".png")
    return [f for f in os.listdir(folder) if f.lower().endswith(supported)]


# Mentés 
def save_image(img, output_folder, original_name, suffix, quality=None, ext_override=None):
    name, ext = os.path.splitext(original_name)

    # alapértelmezett kiterjesztés JPG
    if ext_override is None:
        new_ext = ".jpg"
    else:
        new_ext = ext_override

    output_path = os.path.join(output_folder, f"{name}_{suffix}{new_ext}")

    if quality:
        img.save(output_path, quality=quality)
    else:
        img.save(output_path)

    print("Mentve:", output_path)


# Pixel alapú arányos átméretezés 
def resize_by_width(img, target_width):
    target_width = int(target_width)
    orig_w, orig_h = img.size
    scale = target_width / float(orig_w)
    new_h = int(orig_h * scale)
    return img.resize((target_width, new_h), Image.LANCZOS)



# PNG → JPG 
def convert_png_to_jpg(img):
    return img.convert("RGB")


# JPG → PNG 
def convert_jpg_to_png(img):
    return img


# Menü 
def menu():
    print("\nBatch Képmódosító Program")
    print("1. Képek MÉRET csökkentése (tömörítés)")
    print("2. Képek pixel átméretezése (arányos méretezés)")
    print("3. Fekete-fehér")
    print("4. Elforgatás")
    print("5. Tükrözés")
    print("6. PNG → JPG")
    print("7. JPG → PNG")
    print("8. Kilépés")
    return input("Válassz: ")


# Fő program 
def main():
    print("Mappaválasztás...\n")

    folder = None
    while folder is None:
        folder = choose_folder()

    images = get_images_in_folder(folder)

    output_folder = os.path.join(folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    while True:
        choice = menu()

        # 8. Kilépés
        if choice == "8":
            print("Kilépés...")
            break

        # 1. TÖMÖRÍTÉS (JPEG QUALITY)
        if choice == "1":
            print("\nVálassz tömörítési szintet:")
            print("1. High (90%)")
            print("2. Medium (70%)")
            print("3. Low (40%)")

            opt = input("Választás: ")

            if opt == "1":
                q = 90
            elif opt == "2":
                q = 70
            elif opt == "3":
                q = 40
            else:
                print("Hibás választás!")
                continue

            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                # PNG konvertálása tömörítéshez
                if file.lower().endswith(".png"):
                    img = convert_png_to_jpg(img)

                save_image(img, output_folder, file, f"compressed_{q}", quality=q)

        # 2. PIXEL ÁTMÉRETEZÉS (ÚJ!)
        elif choice == "2":
            print("\nVálassz új szélességet (px):")
            print("1. 1920 px")
            print("2. 1280 px")
            print("3. 800 px")

            opt = input("Választás: ")

            if opt == "1":
                target_width = 1920
            elif opt == "2":
                target_width = 1280
            elif opt == "3":
                target_width = 800
            else:
                print("Hibás választás!")
                continue

            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                resized = resize_by_width(img, target_width)
                save_image(resized, output_folder, file, f"resized_{target_width}px")

        # 3. FEKETE-FEHÉR
        elif choice == "3":
            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                bw = img.convert("L")
                save_image(bw, output_folder, file, "bw")

        # 4. ELFORGATÁS
        elif choice == "4":
            angle = int(input("Hány fokkal forgassam? (90, 180, 270): "))
            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                rot = img.rotate(angle, expand=True)
                save_image(rot, output_folder, file, f"rotated")

        # 5. TÜKRÖZÉS
        elif choice == "5":
            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

                flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
                save_image(flipped, output_folder, file, "flipped")

        # 6. PNG → JPG
        elif choice == "6":
            for file in images:
                if file.lower().endswith(".png"):
                    path = os.path.join(folder, file)
                    img = Image.open(path)

                    jpg = convert_png_to_jpg(img)
                    save_image(jpg, output_folder, file, "png_to_jpg", ext_override=".jpg")
                else:
                    print(f"{file} nem PNG → kihagyva!")

        # 7. JPG → PNG
        elif choice == "7":
            for file in images:
                if file.lower().endswith((".jpg", ".jpeg")):
                    path = os.path.join(folder, file)
                    img = Image.open(path)

                    save_image(img, output_folder, file, "jpg_to_png", ext_override=".png")
                else:
                    print(f"{file} nem JPG → kihagyva!")

        print("\nMinden kép feldolgozva!\n")


if __name__ == "__main__":
    main()
