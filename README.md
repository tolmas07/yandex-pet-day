# Yandex Pet Day — Landing Page

Конференция для разработчиков, дизайнеров и продуктов в сфере зообизнеса и сервисов для животных.

## Technologies

- HTML5 (semantic markup)
- CSS3 (custom properties, Grid, Flexbox, animations)
- Vanilla JavaScript (ES6+)

## Features

- Fully responsive design (1440px desktop + 360px mobile)
- Fixed header with blur effect on scroll
- Mobile burger menu with fullscreen navigation
- Scroll reveal animations (IntersectionObserver)
- FAQ accordion
- Form validation with visual feedback
- Popup modal with keyboard support (Escape to close)
- Scroll-to-top button
- Accessibility: ARIA labels, focus-visible states, semantic HTML

## Structure

```
├── index.html        # Main HTML file
├── css/
│   └── style.css     # All styles
├── js/
│   └── main.js       # All JavaScript
└── README.md
```

## How to run

Open `index.html` in a browser or use a local server:

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```
