// ===== Header scroll =====
const header = document.getElementById('header');
const scrollTopBtn = document.getElementById('scroll-top');

window.addEventListener('scroll', () => {
  const y = window.scrollY;
  header.classList.toggle('scrolled', y > 20);
  scrollTopBtn.classList.toggle('visible', y > 500);
}, { passive: true });

scrollTopBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ===== Mobile menu =====
const burger = document.getElementById('burger');
const mobileNav = document.getElementById('mobile-nav');

burger.addEventListener('click', () => {
  const isOpen = mobileNav.classList.contains('active');
  burger.classList.toggle('active');
  mobileNav.classList.toggle('active');
  burger.setAttribute('aria-expanded', !isOpen);
  document.body.style.overflow = isOpen ? '' : 'hidden';
});

mobileNav.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    burger.classList.remove('active');
    mobileNav.classList.remove('active');
    burger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  });
});

// ===== FAQ accordion =====
document.querySelectorAll('.faq-item__q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.parentElement;
    const isOpen = item.classList.contains('open');

    document.querySelectorAll('.faq-item').forEach(i => {
      i.classList.remove('open');
      i.querySelector('.faq-item__q').setAttribute('aria-expanded', 'false');
    });

    if (!isOpen) {
      item.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
    }
  });
});

// ===== Form validation =====
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function validateForm(form, fields) {
  let valid = true;
  fields.forEach(({ name, type }) => {
    const group = form.querySelector(`[name="${name}"]`).closest('.form-group');
    const value = form.querySelector(`[name="${name}"]`).value.trim();
    let fieldValid = true;

    if (type === 'email') {
      fieldValid = value && validateEmail(value);
    } else {
      fieldValid = value.length > 0;
    }

    group.classList.toggle('error', !fieldValid);
    if (!fieldValid) valid = false;
  });
  return valid;
}

function clearErrors(form) {
  form.querySelectorAll('.form-group').forEach(g => g.classList.remove('error'));
}

// ===== Registration form =====
const registerForm = document.getElementById('register-form');
const registerSuccess = document.getElementById('register-success');

registerForm.addEventListener('submit', (e) => {
  e.preventDefault();
  clearErrors(registerForm);

  if (validateForm(registerForm, [
    { name: 'name', type: 'text' },
    { name: 'surname', type: 'text' },
    { name: 'email', type: 'email' },
    { name: 'format', type: 'text' }
  ])) {
    registerForm.style.display = 'none';
    registerSuccess.classList.add('active');
  }
});

// ===== Popup =====
const popupOverlay = document.getElementById('popup-overlay');
const popupClose = document.getElementById('popup-close');
const openPopupBtn = document.getElementById('open-popup');
const popupForm = document.getElementById('popup-form');
const popupSuccess = document.getElementById('popup-success');

function openPopup() {
  popupOverlay.classList.add('active');
  document.body.style.overflow = 'hidden';
  popupClose.focus();
}

function closePopup() {
  popupOverlay.classList.remove('active');
  document.body.style.overflow = '';
  openPopupBtn.focus();
}

openPopupBtn.addEventListener('click', openPopup);
popupClose.addEventListener('click', closePopup);

popupOverlay.addEventListener('click', (e) => {
  if (e.target === popupOverlay) closePopup();
});

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && popupOverlay.classList.contains('active')) {
    closePopup();
  }
});

popupForm.addEventListener('submit', (e) => {
  e.preventDefault();
  clearErrors(popupForm);

  if (validateForm(popupForm, [
    { name: 'name', type: 'text' },
    { name: 'email', type: 'email' },
    { name: 'question', type: 'text' }
  ])) {
    popupForm.style.display = 'none';
    popupSuccess.classList.add('active');
  }
});

// ===== Scroll reveal =====
const revealElements = document.querySelectorAll(
  '.benefit-card, .speaker-card, .highlight-card, .program__item, .faq-item'
);

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

revealElements.forEach(el => {
  el.classList.add('reveal');
  revealObserver.observe(el);
});

// ===== Smooth scroll for anchor links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});
