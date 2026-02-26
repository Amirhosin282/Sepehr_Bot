# Sepehr Electronic Bot 🤖⚡

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)

Bot ID: @sepehrelectronic_bot

Sepehr Electronic is a Telegram bot built using Python and Telethon.  
The project was developed mainly for learning async architecture,  
event-driven programming, and Telegram automation.

⚠️ The market price API is currently NOT working due to external service issues.  
Since this project was created for learning purposes, it is unlikely to receive future updates.

---

## 🚀 Features

• Async event-driven structure  
• Admin role management  
• Broadcast messaging system  
• Question submission + reply workflow  
• UUID-based tracking system  
• Excel-based lightweight storage  
• Config separation via env directory  

---

## 📦 Project Structure

```
.
├── data
│   ├── answerd_questions.txt     # Stores answered question IDs
│   ├── sepehr_bot.session        # Auto-generated Telethon session
│   ├── usefull_sites.pdf         # Static file sent by bot
│   └── users.xlsx                # User database (auto-created)
├── env
│   ├── admin.txt                 # Admin chat IDs (comma-separated)
│   ├── api_hash.txt              # Telegram API hash
│   ├── api_id.txt                # Telegram API ID
│   ├── api_key.txt               # Market API key (currently inactive)
│   └── token.txt                 # Bot token from BotFather
├── LICENSE
├── main.py
└── README.md
```

---

## ⚙️ Setup Guide

1) Clone the repository  
2) Create the env folder (if not exists)  
3) Fill required configuration files:

env/api_id.txt  
→ Your Telegram API ID  

env/api_hash.txt  
→ Your Telegram API Hash  

env/token.txt  
→ Bot token from BotFather  

env/admin.txt  
→ Admin chat IDs separated by commas  

Example:
```
123456789,987654321
```

---

## 📌 Important Notes

• data/sepehr_bot.session is auto-generated — do NOT edit manually.  
• users.xlsx will be created automatically.  
• Keep sensitive files (env folder, session files) inside .gitignore.  
• This project is educational and not production-grade.  
• API feature is disabled until external service becomes stable.  

---

# ربات سپهر الکترونیک 🤖⚡

شناسه ربات: @sepehrelectronic_bot  

ربات سپهر الکترونیک با استفاده از Python و Telethon ساخته شده است.  
هدف اصلی این پروژه، یادگیری معماری asynchronous،  
برنامه‌نویسی رویدادمحور و کار با API تلگرام بوده است.

⚠️ در حال حاضر API مربوط به قیمت بازار به دلیل مشکلات سرویس‌دهنده خارجی کار نمی‌کند.  
از آنجایی که این پروژه با هدف آموزشی توسعه داده شده، احتمال دریافت آپدیت در آینده پایین است.

---

## 🚀 امکانات

• ساختار async و رویدادمحور  
• مدیریت ادمین‌ها  
• سیستم ارسال پیام همگانی (Broadcast)  
• ثبت سؤال کاربران و پاسخ‌دهی توسط ادمین  
• رهگیری سؤالات با UUID  
• ذخیره‌سازی سبک با Excel  
• جداسازی تنظیمات در پوشه env  

---

## 📦 ساختار پروژه

```
.
├── data
│   ├── answerd_questions.txt     # شناسه سؤالات پاسخ داده شده
│   ├── sepehr_bot.session        # فایل سشن (خودکار ساخته می‌شود)
│   ├── usefull_sites.pdf         # فایل ثابت ارسالی توسط ربات
│   └── users.xlsx                # دیتابیس کاربران (خودکار ساخته می‌شود)
├── env
│   ├── admin.txt                 # آیدی عددی ادمین‌ها (با کاما جدا شود)
│   ├── api_hash.txt              # API Hash تلگرام
│   ├── api_id.txt                # API ID تلگرام
│   ├── api_key.txt               # کلید API بازار (فعلاً غیرفعال)
│   └── token.txt                 # توکن ربات
├── LICENSE
├── main.py
└── README.md
```

---

## ⚙️ راه‌اندازی

1) پروژه را clone کنید  
2) پوشه env را بسازید (در صورت نبود)  
3) فایل‌های تنظیمات را پر کنید  

api_id.txt → API ID  
api_hash.txt → API Hash  
token.txt → توکن ربات  
admin.txt → آیدی عددی ادمین‌ها (با کاما جدا شود)

مثال:
```
123456789,987654321
```

---

## 📌 نکات مهم

• فایل sepehr_bot.session به‌صورت خودکار ساخته می‌شود.  
• users.xlsx در اجرای اولیه ساخته خواهد شد.  
• پوشه env و فایل‌های حساس را در .gitignore قرار دهید.  
• این پروژه در سطح آموزشی است و برای محیط production طراحی نشده است.  
• قابلیت API بازار تا زمان پایدار شدن سرویس‌دهنده غیرفعال است.  