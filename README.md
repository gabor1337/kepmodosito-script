### Képmódosító Script

Ez a projekt egy Python alapú **batch képmódosító program**, amely egyszerre több képet képes feldolgozni egy kiválasztott mappából.  
A script grafikus mappaválasztóval működik, majd a felhasználó által kiválasztott műveletet **minden képre automatikusan alkalmazza**.

A program kifejezetten alkalmas nagy mennyiségű kép gyors feldolgozására.

-----------------------

### Funkciók

A program az alábbi műveleteket támogatja:

### 1. Képek tömörítése (JPEG quality)
A fájlméret csökkentése a minőség arányos csökkentésével:
- High (90%)
- Medium (70%)
- Low (40%)

PNG képek automatikusan JPG-vé konvertálódnak tömörítés előtt.

-----------------------

### 2. Képek pixel átméretezése (arányos)
A képek szélessége módosítható, miközben a magasság automatikusan arányosan változik.  
Választható cél szélességek:

- 1920 px
- 1280 px
- 800 px

A képek arányukat megtartják, torzítás nélkül.

-----------------------

### 3. Fekete-fehér konverzió (grayscale)

Minden kép fekete-fehér változata elkészül, `.jpg` formátumban mentve.

-----------------------

### 4. Képek elforgatása
A felhasználó által megadott szögben:

- 90°
- 180°
- 270°

-----------------------

### 5. Képek tükrözése
Bal–jobb irányú tükrözés minden képen.

-----------------------

###  6. PNG → JPG átalakítás
###  7. JPG → PNG átalakítás

Mindkét irányú konverzió automatikusan, batch módban működik.

-----------------------

### Kimenet

A feldolgozott képek a következő helyre kerülnek:
  output mappába

A fájlnevek automatikusan kiegészülnek a művelet jelölésével, pl.:

  kep1_resized_800px.jpg
  
  kep2_compressed_70.jpg
  
  kep3_bw.jpg
  
  kep4_rotated.jpg
  
  kep5_png_to_jpg.jpg
  
-----------------------

### Telepítés

A program futtatásához Python és két csomag szükséges:

pip install pillow
pip install tk

-----------------------

### Használat:

I. Futtasd a programot: Futtasd a programot:

II. Válaszd ki a képeket tartalmazó mappát (egy fájlböngésző ablak jelenik meg).

III. Válassz egy funkciót a menüből:

  1. Képek tömörítése
  2. Képek pixel átméretezése (arányos)
  3. Fekete-fehér
  4. Elforgatás
  5. Tükrözés
  6. PNG → JPG
  7. JPG → PNG
  8. Kilépés

IV. A program elvégzi a műveletet minden képen automatikusan.

-----------------------

### Projekt felépítése
   project/
        │
  
  ├── main.py         # A program fő fájlja
  
  ├── README.md       # Dokumentáció
  
  └── output/         # Ide mentődnek a feldolgozott képek

-----------------------

### Készítők:
  Borics Gergő Bendegúz
  
  Molnár Gábor

-----------------------

### Licenc
  A projekt MIT licenc alatt érhető el.
