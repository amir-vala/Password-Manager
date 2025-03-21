# Password Manager

## Introduction
Password Manager is a Python-based tool that helps users generate, encrypt, store, and retrieve passwords securely. It uses AES encryption for password security and bcrypt for authentication. The application provides a command-line interface for ease of use.

## Features
- Generate strong random passwords with customizable length and character restrictions.
- Encrypt and store passwords securely using AES encryption.
- Securely save and retrieve passwords using JSON files.
- Authenticate users with a hashed password stored in `apppass.json`.
- Retrieve saved passwords securely with decryption.

## Installation
1. **Clone the repository or create a project folder:**
    ```bash
    mkdir PasswordManager
    cd PasswordManager
    ```
2. **Ensure Python is installed (Python 3.6 or higher is recommended).**
3. **(Optional) Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
    Activate it using:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the script:
    ```bash
    python password_manager.py
    ```
2. Follow the on-screen instructions to generate and manage passwords.

## Files & Structure
- `password_manager.py` - Main script for password management.
- `apppass.json` - Stores the hashed master password.
- `passwords.json` - Stores encrypted passwords.
- `key.json` - Stores encryption keys.
- `requirements.txt` - Lists required dependencies.

## Security Notes
- **DO NOT lose your master password.** If lost, all stored passwords will be unrecoverable.
- Passwords and encryption keys are stored in JSON files but encrypted using AES.
- The tool does not share passwords or store them in plain text.

## Future Improvements
- Implement a graphical user interface (GUI).
- Add support for multi-user password management.
- Enhance error handling and security measures.

---

# مدیر رمز عبور

## معرفی
مدیر رمز عبور یک ابزار مبتنی بر پایتون است که به کاربران کمک می‌کند تا رمزهای عبور قوی ایجاد، رمزگذاری، ذخیره و بازیابی کنند. این برنامه از رمزگذاری AES برای امنیت رمزهای عبور و bcrypt برای احراز هویت استفاده می‌کند. این برنامه یک رابط کاربری کنسولی برای استفاده آسان ارائه می‌دهد.

## ویژگی‌ها
- تولید رمزهای عبور قوی با طول و محدودیت‌های کاراکتری سفارشی.
- رمزگذاری و ذخیره امن رمزهای عبور با استفاده از AES.
- ذخیره و بازیابی امن رمزهای عبور در فایل‌های JSON.
- احراز هویت کاربران با رمز عبور هش‌شده در `apppass.json`.
- بازیابی رمزهای عبور ذخیره‌شده با رمزگشایی امن.

## نصب
1. **مخزن را کلون کنید یا یک پوشه پروژه ایجاد کنید:**
    ```bash
    mkdir PasswordManager
    cd PasswordManager
    ```
2. **اطمینان حاصل کنید که پایتون نصب شده است (ترجیحاً نسخه ۳.۶ یا بالاتر).**
3. **(اختیاری) ایجاد محیط مجازی:**
    ```bash
    python -m venv venv
    ```
    فعال‌سازی:
    - ویندوز: `venv\Scripts\activate`
    - لینوکس/macOS: `source venv/bin/activate`
4. **نصب وابستگی‌ها:**
    ```bash
    pip install -r requirements.txt
    ```

## نحوه استفاده
1. اجرای برنامه:
    ```bash
    python password_manager.py
    ```
2. دستورالعمل‌های روی صفحه را دنبال کنید تا رمزهای عبور را مدیریت کنید.

## ساختار فایل‌ها
- `password_manager.py` - اسکریپت اصلی برای مدیریت رمز عبور.
- `apppass.json` - ذخیره رمز عبور اصلی به‌صورت هش شده.
- `passwords.json` - ذخیره رمزهای عبور رمزگذاری شده.
- `key.json` - ذخیره کلیدهای رمزگذاری.
- `requirements.txt` - شامل لیست وابستگی‌های موردنیاز.

## نکات امنیتی
- **رمز عبور اصلی خود را فراموش نکنید.** در صورت فراموشی، هیچ راهی برای بازیابی رمزهای عبور ذخیره شده وجود ندارد.
- رمزهای عبور و کلیدهای رمزگذاری در فایل‌های JSON ذخیره شده‌اند اما با استفاده از AES رمزگذاری می‌شوند.
- این ابزار رمزهای عبور را به‌صورت متن ساده ذخیره نمی‌کند و به اشتراک نمی‌گذارد.

## بهبودهای آینده
- اضافه کردن رابط کاربری گرافیکی (GUI).
- پشتیبانی از مدیریت رمز عبور برای چند کاربر.
- بهبود کنترل خطاها و افزایش تدابیر امنیتی.

