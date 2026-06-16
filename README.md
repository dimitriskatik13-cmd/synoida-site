# Σύνοιδα — Demo Site

Στατικό website (HTML + Tailwind ενσωματωμένο τοπικά). **Δεν χρειάζεται build ή server** για να τρέξει — απλά static αρχεία.

## Τοπική προβολή
Άνοιξε το `index.html` στον browser, ή σέρβιρέ το τοπικά:
```bash
python3 -m http.server 8000
# → http://localhost:8000
```

## Δημοσίευση σε GitHub Pages

**Επιλογή Α — μέσω terminal (git):**
1. Φτιάξε ένα νέο **public** repo στο https://github.com/new (π.χ. `synoida-site`) — χωρίς README/.gitignore.
2. Από αυτόν τον φάκελο:
   ```bash
   git remote add origin https://github.com/<USERNAME>/synoida-site.git
   git push -u origin main
   ```
3. Στο repo: **Settings → Pages → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**.
4. Σε ~1 λεπτό θα είναι live στο: `https://<USERNAME>.github.io/synoida-site/`

**Επιλογή Β — χωρίς terminal (web upload):**
1. Νέο public repo στο github.com.
2. **Add file → Upload files** → σύρε ΟΛΑ τα περιεχόμενα αυτού του φακέλου → **Commit**.
3. Ίδιο βήμα 3 & 4 με πάνω (Settings → Pages).

## Δομή φακέλου
- `*.html` — οι 13 σελίδες (το live site)
- `assets/` — εικόνες, λογότυπα, και το Tailwind (vendored, για offline λειτουργία)
- `_build/` — το σύστημα παραγωγής: `template.html` (κοινό κέλυφος) + `fragments/` (το `<main>` κάθε σελίδας) + `build.py`. Τρέξε `python3 _build/build.py` για να ξαναχτιστούν οι σελίδες μετά από αλλαγή.
- `reference-pages/` — το πραγματικό κείμενο κάθε σελίδας (τραβηγμένο από το synoida.gr)

## Σημειώσεις για τον developer
- Παλέτα/τυπογραφία/components ορίζονται μία φορά στο `_build/template.html` (Tailwind config + brand tokens: green `#8DC63F`, red `#ED1C24`, blue `#00AEEF`, orange `#F7941D`, grey `#58595B`). Comfortaa (τίτλοι) + Inter (κείμενο).
- Όλα τα links είναι **relative**, οπότε δουλεύει και σε subpath (`/synoida-site/`).
- Το κείμενο είναι το πραγματικό περιεχόμενο του synoida.gr.
