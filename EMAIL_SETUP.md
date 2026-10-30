# Oziq Ovqat — Email tizimi sozlash

## 1. Gmail App Password

1. Google Account → **Security** → 2-Step Verification yoqing.
2. **App passwords** → "Mail" / "Other" → 16 belgilik parol oling.
3. Oddiy Gmail parolini **EMAIL_HOST_PASSWORD** ga qo‘ymang — faqat App Password.

## 2. Lokal `.env` (loyiha ildizida)

```env
DJANGO_SECRET_KEY=uzun-random-kalit
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
SITE_URL=http://127.0.0.1:8000
DEFAULT_FROM_EMAIL=Oziq Ovqat <your-gmail@gmail.com>
ADMIN_NOTIFY_EMAIL=your-gmail@gmail.com

# Lokal test — konsolga chiqaradi
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Haqiqiy SMTP (Gmail)
# EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=xxxx-xxxx-xxxx-xxxx
```

## 3. Render / PythonAnywhere Environment Variables

Hosting **Environment** bo‘limiga quyidagilarni qo‘ying (`.env` fayl yuklash shart emas):

| Variable | Misól qiymat |
|----------|--------------|
| `DJANGO_SECRET_KEY` | uzun random |
| `DJANGO_DEBUG` | `False` |
| `DJANGO_ALLOWED_HOSTS` | `your-app.onrender.com` |
| `SITE_URL` | `https://your-app.onrender.com` |
| `EMAIL_BACKEND` | `django.core.mail.backends.smtp.EmailBackend` |
| `EMAIL_HOST` | `smtp.gmail.com` |
| `EMAIL_PORT` | `587` |
| `EMAIL_USE_TLS` | `True` |
| `EMAIL_HOST_USER` | Gmail manzil |
| `EMAIL_HOST_PASSWORD` | App Password |
| `DEFAULT_FROM_EMAIL` | `Oziq Ovqat <your-gmail@gmail.com>` |
| `ADMIN_NOTIFY_EMAIL` | admin email |

## 4. Sinov buyruqlari

```bash
# Console backend bilan
python manage.py shell
>>> from django.contrib.auth.models import User
>>> from apps.email_utils import send_welcome_email
>>> u = User.objects.filter(email__isnull=False).exclude(email="").first()
>>> send_welcome_email(u)

# Yoki ro‘yxatdan o‘tish / buyurtma berish orqali

python manage.py check
python manage.py test apps.tests
```

## 5. Qaysi email qachon ketadi

| Hodisa | Qabul qiluvchi |
|--------|----------------|
| Ro‘yxatdan o‘tish | Foydalanuvchi |
| Buyurtma yaratish | Mijoz (agar user.email bor) + Admin |
| Holat o‘zgarishi (admin panel / Django admin) | Mijoz |
| Parolni tiklash | Foydalanuvchi |

SMTP xatosi ro‘yxatdan o‘tish yoki buyurtmani **buzmaydi** — faqat logga yoziladi.
