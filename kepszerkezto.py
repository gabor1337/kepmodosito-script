import os
from PIL import Image
from tkinter.filedialog import askdirectory
import tkinter as tk

<<<<<<< HEAD
# Mappa kiválasztása
=======

>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a
def choose_folder():
    root = tk.Tk()
    root.withdraw()
    folder = askdirectory(title="Válassz egy mappát a képekhez")
    if folder:
<<<<<<< HEAD
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
=======
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

>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a
    if ext_override is None:
        new_ext = ".jpg"
    else:
        new_ext = ext_override

    output_path = os.path.join(output_folder, f"{name}_{suffix}{new_ext}")
<<<<<<< HEAD

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
=======
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

>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a


# Fő program 
def main():
<<<<<<< HEAD
    print("Mappaválasztás...\n")
=======
    print("Válassz egy mappát a képekhez...\n")
>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a

    folder = None
    while folder is None:
        folder = choose_folder()

    images = get_images_in_folder(folder)
<<<<<<< HEAD
=======
    if not images:
        print("A mappában nincsenek képek!")
        return
>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a

    output_folder = os.path.join(folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    while True:
        choice = menu()

<<<<<<< HEAD
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
=======
        
        if choice == "7":
            print("Kilépés...")
            break

        
        if choice == "1":
            w = int(input("Új szélesség: "))
            h = int(input("Új magasság: "))
>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a

            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

<<<<<<< HEAD
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

=======
                result = resize_image(img, w, h)
                save_image(result, output_folder, file, "resized")

        
        elif choice == "2":
>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a
            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

<<<<<<< HEAD
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
=======
                result = make_bw(img)
                save_image(result, output_folder, file, "bw")

        
        elif choice == "3":
            angle = int(input("Hány fokkal forgassam? (90, 180, 270): "))

>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a
            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)

<<<<<<< HEAD
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
=======
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
>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a
                if file.lower().endswith(".png"):
                    path = os.path.join(folder, file)
                    img = Image.open(path)

<<<<<<< HEAD
                    jpg = convert_png_to_jpg(img)
                    save_image(jpg, output_folder, file, "png_to_jpg", ext_override=".jpg")
                else:
                    print(f"{file} nem PNG → kihagyva!")

        # 7. JPG → PNG
        elif choice == "7":
=======
                    result = convert_png_to_jpg(img)
                    save_image(result, output_folder, file, "png_to_jpg", ".jpg")
                else:
                    print(f"{file} nem PNG, kihagyva!")

       
        elif choice == "6":
>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a
            for file in images:
                if file.lower().endswith((".jpg", ".jpeg")):
                    path = os.path.join(folder, file)
                    img = Image.open(path)

<<<<<<< HEAD
                    save_image(img, output_folder, file, "jpg_to_png", ext_override=".png")
                else:
                    print(f"{file} nem JPG → kihagyva!")
=======
                    result = convert_jpg_to_png(img)
                    save_image(result, output_folder, file, "jpg_to_png", ".png")
                else:
                    print(f"{file} nem JPG, kihagyva!")

        else:
            print("Hibás választás!")
            continue
>>>>>>> 2a3dd2aaf9c896c6b37934094189c36547a39c9a

        print("\nMinden kép feldolgozva!\n")


if __name__ == "__main__":
    main()
