# Template projekt za NOO za Github classroom

Ta repozitorij je predloga (template) za reševanje nalog v GitHub Classroom. Vključuje pripravljeno strukturo za pisanje kode, testiranje rešitev ter avtomatsko preverjanje z GitHub Actions.

---

## Struktura projekta
Projekt naj ima strukturo:
```
noo-template/  # Daj svoje ime
├── .github/
│ └── workflows/
│ |  └── classroom.yml # GitHub Actions workflow za ocenjevanje
├── notebook.ipynb # Glavni zvezek za reševanje naloge
├── requirements.txt # Potrebne knjižnice
├── README.md # Navodila za uporabo
└── .gitignore # Izključene datoteke (npr. pycache)
```

---

## Cilj

- Študent dopolni manjkajoče dele v `notebook.ipynb`
- Shrani svoje odgovore in odgovori na teoretična vprašanja
- Požene celice, ki ustvarijo datoteko `odgovori.json`
- Svoje rešitve **shrani in potisne (push)** v GitHub

Po vsakem potisku (`git push`) se samodejno zažene GitHub Actions, ki:
1. Pretvori `notebook.ipynb` v `.py` datoteko
2. Prenese skrite teste iz zunanjega repozitorija
3. Zažene `pytest` in preveri rešitve
4. Ustvari `grade_summary.json` (točkovanje)
5. Naloži rezultate kot artefakt v zavihku "Actions"

---

## Avtomatsko preverjanje (CI)

**Workflow datoteka:** `.github/workflows/classroom.yml`

Ta datoteka vsebuje:
- Navodila za nastavitev Pythona in knjižnic
- Ukaz za pretvorbo zvezka:
  ```bash
  jupyter nbconvert --to notebook --execute notebook.ipynb --inplace
  jupyter nbconvert --to python notebook.ipynb --output=student_code.py
- Prenos testne skripte:
  ```
  curl -o tests.py https://raw.githubusercontent.com/lhrs-workshops/noo-tests/refs/heads/main/test_template.py
  ```
- Zagon testov:
  ```
  pytest tests.py --disable-warnings -v
  ```
- Naložitev rezultatov v oddajo kot artifact
  ```
  - name: Naloži rezultate
  uses: actions/upload-artifact@v4
  with:
    name: grade-summary
    path: grade_summary.json
  ```

## Navodila za študente
1. Študent pošljite link na nalogo iz GH classroom
2. Odpre notebook.ipynb v Jupyter okolju (npr. VS Code, JupyterLab)
3. Implementira manjkajočo logiko
4. Odgovori na teoretična vprašanja z uporabo izbirnikov
5. Zažene celico, ki shrani tvoje odgovore v odgovori.json
6. Izvede ukaze:
```
git add .
git commit -m "rešena naloga"
git push
```
7. Po potisku bo GitHub avtomatsko preveril rešitev in ustvaril rezultate.

## Kako pregledovalec vidi rezultate
Rezultati testiranja za vsakega študenta se nahajajo pod Actions > [ime potiska] > Artifacts > grade-summary

Vsebina grade_summary.json:
```
{
  "square": true,
  "is_even": true,
  "q1": true,
  "q2": false,
  "total_score": 3,
  "max_score": 4
}
```

## Razširjanje naloge
Če želiš dodati nove naloge:
 - Zamenjaj notebook.ipynb z novo nalogo
 - Pripravi nove teste v zunanjem testnem repozitoriju
 - Posodobi URL v classroom.yml, če se testna datoteka spremeni (npr. test_funkcije.py)
 -❗ Pomembno odgovori.json mora biti ustvarjen v Jupyter zvezku pred oddajo
 - Če pytest ne najde datoteke, bo test padel
 - Če študent spremeni imena funkcij, bodo testi neuspešni


## Projekt definiraj kot template
V projektu je potrebno nastaviti kot template:
```
Settings -> General -> Template repository
```
