# Travel Card Vending Machine (TCVM)

The **Travel Card Vending Machine (TCVM)** is a web-based application designed to automate and simplify metro travel card services. This system enables passengers to register, recharge, and manage travel cards used for traveling across five different metro zones. Built using **HTML, CSS, JavaScript, and Django**, TCVM replaces the traditional ticketing system, reducing human effort and time.

---

## 🌟 Features

### 👤 User Functions
- **User Registration** with personal details and valid ID proof
- **Card Issuance** after successful registration and payment
- **Card Recharge** via integrated credit/debit card payment
- **Account Deletion** for users who no longer need the service

### 🛠️ Admin Functions
- Monitor and manage all **user registrations** and **payment transactions**

### ⚙️ System Functions
- **Card Reading**: Detect and authenticate both travel and bank cards
- **Receipt Generation**: Automatically print receipts for all transactions
- **Display Information** related to transactions and card status

---

## ✅ Functional Requirements (Implemented)
- [x] Register: New user sign-up with validation
- [x] Card Printing: Display user details and paid amount on virtual card
- [x] Login: Card-based login system for registered users
- [x] Payment: Integrated payment gateway for adding funds

---

## 🖥️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Django (Python)
- **Database**: SQLite (default Django DB)
- **Version Control**: Git & GitHub

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/tcvm.git
   cd tcvm
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

6. Open in browser: `http://127.0.0.1:8000/`

---

## 📸 Screenshots

> *(Add screenshots of the UI for login, registration, card printing, etc.)*

---

## 📌 Future Enhancements

- Zone-wise fare calculation based on journey
- NFC-based card reading
- Transaction history view/download for users
- Admin dashboard with analytics

---

## 🤝 Contributors

- [Your Name 1](https://github.com/username1)
- [Your Name 2](https://github.com/username2)
- [Your Name 3](https://github.com/username3)
- [Your Name 4](https://github.com/username4)

---

## 📄 License

This project is for educational purposes as part of the Software Engineering Lab and is not licensed for commercial use.

---

## 💬 Feedback

Feel free to open issues or submit pull requests if you'd like to contribute or suggest improvements.
