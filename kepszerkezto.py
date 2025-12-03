import os
from PIL import Image
from tkinter.filedialog import askdirectory
import tkinter as tk



# --- Mappa kiválasztása ---
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



# --- Képek listázása ---
def get_images_in_folder(folder):
    supported = (".jpg", ".jpeg", ".png", ".bmp")
    return [f for f in os.listdir(folder) if f.lower().endswith(supported)]



# --- Mentés ---
def save_image(img, output_folder, original_name, suffix, quality=None, ext_override=None):
    name, ext = os.path.splitext(original_name)


    # alapértelmezett formátum JPG
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



# --- Arányos átméretezés ---
def resize_by_width(img, target_width):
    target_width = int(target_width)
    orig_w, orig_h = img.size
    scale = target_width / float(orig_w)
    new_h = int(orig_h * scale)
    return img.resize((target_width, new_h), Image.LANCZOS)



# --- Képkivágás (Crop) ---
def crop_image(img, left, top, right, bottom):
    """
    Képkivágás a megadott koordináták alapján.
    left, top: bal felső sarok
    right, bottom: jobb alsó sarok
    """
    return img.crop((left, top, right, bottom))


def crop_center(img, crop_width, crop_height):
    """
    Középről kivágás a megadott szélességgel és magassággal.
    """
    orig_w, orig_h = img.size
    left = (orig_w - crop_width) // 2
    top = (orig_h - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    return img.crop((left, top, right, bottom))


def crop_aspect_ratio(img, aspect_w, aspect_h):
    """
    Képarány szerinti kivágás (középről).
    Pl: 16:9, 4:3, 1:1
    """
    orig_w, orig_h = img.size
    target_ratio = aspect_w / aspect_h
    orig_ratio = orig_w / orig_h

    if orig_ratio > target_ratio:
        # Túl széles, levágunk oldalról
        new_w = int(orig_h * target_ratio)
        new_h = orig_h
    else:
        # Túl magas, levágunk felül/alul
        new_w = orig_w
        new_h = int(orig_w / target_ratio)

    return crop_center(img, new_w, new_h)



# --- Konverziók ---
def convert_png_to_jpg(img):
    return img.convert("RGB")



def convert_jpg_to_png(img):
    return img



# --- Menü ---
def menu():
    print("\n=== Batch Képmódosító Program ===")
    print("1. Képek tömörítése (méretcsökkentés)")
    print("2. Képek pixel átméretezése (arányos)")
    print("3. Fekete-fehér")
    print("4. Elforgatás")
    print("5. Tükrözés")
    print("6. PNG → JPG átalakítás")
    print("7. JPG → PNG átalakítás")
    print("8. Képkivágás (Crop)")
    print("9. Kilépés")
    return input("Válassz: ")



# --- Fő program ---
def main():


    print("Mappaválasztás...\n")


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


        # Kilépés
        if choice == "9":
            print("Kilépés...")
            break


        # 1. Tömörítés
        if choice == "1":
            print("\nTömörítés szintje:")
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


                if file.lower().endswith(".png"):
                    img = convert_png_to_jpg(img)


                save_image(img, output_folder, file, f"compressed_{q}", quality=q)


        # 2. Pixel átméretezés
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


        # 3. Fekete-fehér
        elif choice == "3":
            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)


                bw = img.convert("L")
                save_image(bw, output_folder, file, "bw")


        # 4. Elforgatás
        elif choice == "4":
            angle = int(input("Hány fokkal forgassam? (90, 180, 270): "))


            for file in images:
                path = os.path.join(folder, file)
                img = Image.open(path)


                rot = img.rotate(angle, expand=True)
                save_image(rot, output_folder, file, f"rotated")


        # 5. Tükrözés
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


        # 8. Képkivágás (Crop)
        elif choice == "8":
            print("\nKépkivágás módja:")
            print("1. Képarány szerinti kivágás (középről)")
            print("2. Fix méret kivágása (középről)")
            print("3. Egyedi koordináták megadása")

            crop_opt = input("Választás: ")

            if crop_opt == "1":
                print("\nVálassz képarányt:")
                print("1. 16:9 (szélesvásznú)")
                print("2. 4:3 (hagyományos)")
                print("3. 1:1 (négyzet)")
                print("4. 9:16 (álló, pl. Instagram Story)")
                print("5. 3:2 (fotó)")

                ar_opt = input("Választás: ")
                aspect_ratios = {
                    "1": (16, 9),
                    "2": (4, 3),
                    "3": (1, 1),
                    "4": (9, 16),
                    "5": (3, 2)
                }

                if ar_opt not in aspect_ratios:
                    print("Hibás választás!")
                    continue

                aspect_w, aspect_h = aspect_ratios[ar_opt]

                for file in images:
                    path = os.path.join(folder, file)
                    img = Image.open(path)
                    cropped = crop_aspect_ratio(img, aspect_w, aspect_h)
                    save_image(cropped, output_folder, file, f"crop_{aspect_w}x{aspect_h}")

            elif crop_opt == "2":
                print("\nAdd meg a kivágás méretét:")
                crop_width = int(input("Szélesség (px): "))
                crop_height = int(input("Magasság (px): "))

                for file in images:
                    path = os.path.join(folder, file)
                    img = Image.open(path)
                    orig_w, orig_h = img.size

                    # Ellenőrzés, hogy a kép elég nagy-e
                    if crop_width > orig_w or crop_height > orig_h:
                        print(f"{file} túl kicsi ehhez a kivágáshoz → kihagyva!")
                        continue

                    cropped = crop_center(img, crop_width, crop_height)
                    save_image(cropped, output_folder, file, f"crop_{crop_width}x{crop_height}")

            elif crop_opt == "3":
                print("\nAdd meg a kivágás koordinátáit:")
                print("(A kép bal felső sarka: 0, 0)")
                left = int(input("Bal (left) px: "))
                top = int(input("Felső (top) px: "))
                right = int(input("Jobb (right) px: "))
                bottom = int(input("Alsó (bottom) px: "))

                for file in images:
                    path = os.path.join(folder, file)
                    img = Image.open(path)
                    orig_w, orig_h = img.size

                    # Ellenőrzés
                    if right > orig_w or bottom > orig_h or left >= right or top >= bottom:
                        print(f"{file} koordináták hibásak → kihagyva!")
                        continue

                    cropped = crop_image(img, left, top, right, bottom)
                    save_image(cropped, output_folder, file, f"crop_custom")

            else:
                print("Hibás választás!")
                continue


        print("\nMinden kép feldolgozva!\n")



if __name__ == "__main__":
    main()
