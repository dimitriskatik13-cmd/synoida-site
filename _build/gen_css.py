#!/usr/bin/env python3
"""Παράγει το assets/site.css από τις built σελίδες.

Τρόπος λειτουργίας: μαζεύει όλα τα class attributes από τα example/*.html,
τα βάζει σε μια συνθετική σελίδα που φορτώνει το τοπικό _build/tailwind.js
(Play CDN runtime) + το config, την ανοίγει σε headless Chromium και
αποθηκεύει το CSS που παρήγαγε το runtime ως στατικό assets/site.css.
Έτσι οι σελίδες δεν χρειάζονται πλέον το 400KB runtime script.

Τρέχει αυτόματα από το build.py (αν υπάρχει playwright), ή χειροκίνητα:
    python3 _build/gen_css.py
"""
import glob
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # example/
OUT = os.path.join(ROOT, 'assets', 'site.css')
CONFIG = open(os.path.join(HERE, 'tailwind-config.js'), encoding='utf-8').read()

# 1) όλα τα class attributes απ' όλες τις built σελίδες
classes = set()
for f in glob.glob(os.path.join(ROOT, '*.html')):
    src = open(f, encoding='utf-8').read()
    classes.update(re.findall(r'class="([^"]*)"', src))
# κλάσεις που προσθέτει δυναμικά το JS (safelist)
classes.update(['hidden', 'flex', 'rotate-180', 'in', 'nav-active', 'js'])

divs = '\n'.join('<div class="%s"></div>' % html.escape(c, quote=True) for c in sorted(classes))
synth = f"""<!doctype html><html lang="el"><head>
<script src="_build/tailwind.js"></script>
<script>{CONFIG}</script>
</head><body>
{divs}
</body></html>"""

tmp = os.path.join(ROOT, '_gen_tmp.html')
open(tmp, 'w', encoding='utf-8').write(synth)

try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        p = b.new_page()
        p.goto('file://' + tmp, wait_until='networkidle')
        p.wait_for_timeout(400)
        css = p.evaluate("""(() => {
            const styles = Array.from(document.querySelectorAll('style'));
            const tw = styles.filter(s => s.textContent.includes('tailwindcss') || s.textContent.length > 5000);
            return tw.map(s => s.textContent).join('\\n');
        })()""")
        b.close()
    if len(css) < 10000:
        sys.exit('gen_css: το παραγόμενο CSS φαίνεται ελλιπές (%d bytes) — δεν γράφτηκε' % len(css))
    open(OUT, 'w', encoding='utf-8').write(css)
    print('site.css: %d classes -> %d KB' % (len(classes), len(css) // 1024))
finally:
    os.remove(tmp)
