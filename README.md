Hallgató: Balogh Dániel (BD) QN3RRK
Tantárgy: Szkript nyelvek
Beadandó: Edzésnapló alkalmazás

Leírás:
Ez egy edzésnapló alkalmazás, amely lehetővé teszi a felhasználónak, hogy rögzítse a különböző gyakorlatok adatait (dátum, gyakorlat, ismétlés, súly).
Az adatok megjelennek a grafikus felületen, törölhetők, CSV fájlba menthetők, illetve matplotlib segítségével grafikonon is megjeleníthető egy gyakorlat súlyfejlődése.

A program induláskor automatikusan beolvassa a korábbi adatokat a workout_data.csv fájlból.
A teljes felület Tkinterrel készült.

A program indítása: main.py
Az alapablak neve: root
A program példány neve: app

Modulok és függvények:
 bd_workout_module.py
 -BDEdzes osztály
Tárolja az edzésadatokat: dátum, gyakorlat, ismétlés, súly.
Tartalmazza a to_list() metódust a CSV mentéshez.

- bd_max_weight(entries, exercise_name)
Visszaadja egy adott gyakorlat maximális súlyát.

bd_data_handler.py
 Fájlkezelés és dátumkezelés.
- save_to_csv(entries) – adatok mentése
- load_from_csv() – adatok automatikus betöltése indításkor
- format_date() – dátum formázása (datetime modul)

bd_visualize.py
 Grafikon megjelenítése matplotlib segítségével.
- show_weight_progress(entries, exercise_name)
A súlyok időbeli változását jeleníti meg vonaldiagramon.

bd_app.py
 A Tkinter grafikus felület és az eseménykezelések modula.
Kezeli az adatbevitelt, törlést, mentést, grafikon megjelenítését, és a kilépést.

Osztályok:
BDEdzes (bd_workout_module.py)

 Attribútumok:
- date
- exercise
- reps
- weight

 Metódus:
- to_list() – CSV exporthoz