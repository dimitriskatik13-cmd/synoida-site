#!/usr/bin/env python3
"""Assemble all site pages from template.html + per-page <main> fragments."""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # example/
TEMPLATE = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
FRAG = os.path.join(HERE, 'fragments')

# outfile : (title, description, data-page)
PAGES = {
 'index.html':                 ('Αρχική - Σύνοιδα', 'Σύνοιδα — Κέντρα Ειδικών Θεραπειών. 26 χρόνια δίπλα στο παιδί.', 'home'),
 'about-us.html':              ('Σχετικά με μας - Σύνοιδα', 'Η ιστορία, ο τρόπος λειτουργίας και η ομάδα της Σύνοιδα.', 'about'),
 'rating.html':                ('Αξιολόγηση - Σύνοιδα', 'Η διαδικασία αξιολόγησης του παιδιού στη Σύνοιδα.', 'rating'),
 'treatments.html':            ('Θεραπείες - Σύνοιδα', 'Οι θεραπείες της Σύνοιδα για κάθε παιδί.', 'treatments'),
 'adult-diagnosis.html':       ('Διάγνωση Ενηλίκων - Σύνοιδα', 'Διάγνωση ενηλίκων στη Σύνοιδα.', 'adult'),
 'contact-us.html':            ('Επικοινωνία - Σύνοιδα', 'Επικοινωνήστε με τα κέντρα της Σύνοιδα.', 'contact'),
 'treatment-speech.html':      ('Λογοθεραπεία - Σύνοιδα', 'Λογοθεραπεία στη Σύνοιδα.', 'treatments'),
 'treatment-occupational.html':('Εργοθεραπεία - Σύνοιδα', 'Εργοθεραπεία στη Σύνοιδα.', 'treatments'),
 'treatment-special.html':     ('Ειδική Αγωγή - Σύνοιδα', 'Ειδική αγωγή στη Σύνοιδα.', 'treatments'),
 'treatment-psychotherapy.html':('Ψυχοθεραπεία - Σύνοιδα', 'Ψυχοθεραπεία στη Σύνοιδα.', 'treatments'),
 'treatment-consulting.html':  ('Συμβουλευτική - Σύνοιδα', 'Συμβουλευτική γονέων στη Σύνοιδα.', 'treatments'),
 'treatment-play.html':        ('Παιγνιοθεραπεία - Σύνοιδα', 'Παιγνιοθεραπεία στη Σύνοιδα.', 'treatments'),
 'treatment-social.html':      ('Ομάδες Κοινωνικών Δεξιοτήτων - Σύνοιδα', 'Ομάδες κοινωνικών δεξιοτήτων στη Σύνοιδα.', 'treatments'),
}

built, missing = [], []
for outfile, (title, desc, page) in PAGES.items():
    fpath = os.path.join(FRAG, outfile)
    if not os.path.exists(fpath):
        missing.append(outfile); continue
    main = open(fpath, encoding='utf-8').read().strip()
    main = main.replace('<main>', '<main id="main">', 1)   # στόχος του skip link
    out = (TEMPLATE
           .replace('{{TITLE}}', title)
           .replace('{{DESC}}', desc)
           .replace('{{PAGE}}', page)
           .replace('{{MAIN}}', main))
    open(os.path.join(ROOT, outfile), 'w', encoding='utf-8').write(out)
    built.append(outfile)

print('BUILT', len(built), 'pages:', ', '.join(built))
if missing:
    print('MISSING fragments:', ', '.join(missing))
    sys.exit(0 if '--allow-missing' in sys.argv else 1)
