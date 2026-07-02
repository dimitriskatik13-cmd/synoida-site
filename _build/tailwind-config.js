tailwind.config = {
      theme: {
        extend: {
          colors: {
            green:  '#8DC63F',
            red:    '#ED1C24',
            blue:   '#00AEEF',
            orange: '#F7941D',
            grey:   '#58595B',
            ink:    '#58595B',  /* headings + body, per brand */
            /* σκούρες παραλλαγές ΜΟΝΟ για κείμενο (WCAG AA ≥4.5:1 σε λευκό & mist) —
               τα brand hex μένουν ανέγγιχτα σε κουμπιά/εικονίδια/γεμίσματα */
            greenDeep:  '#567A1C',
            redDeep:    '#D9151D',
            blueDeep:   '#0072A3',
            orangeDeep: '#A85D00',
            charcoal:   '#3A3B3C',  /* κείμενο πάνω σε πράσινα κουμπιά (5.5:1) */
            mist:   '#FBF7F0',  /* warm beige — alternating section bg */
            alt:    '#F3ECDE',  /* deeper warm beige */
          },
          fontFamily: {
            display: ['Comfortaa', 'system-ui', 'cursive'],
            sans:    ['Inter', 'system-ui', 'sans-serif'],
          },
          boxShadow: {
            card: '0 14px 38px -20px rgba(88,89,91,.38)',
            soft: '0 6px 20px -12px rgba(88,89,91,.35)',
          },
        },
      },
    };
