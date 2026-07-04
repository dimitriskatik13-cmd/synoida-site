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
