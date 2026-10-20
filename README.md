# 🔐 Password Strength Checker

A simple command-line tool written in Python that checks how strong a password is and gives tips to improve it.

> Built as a beginner cybersecurity project.

## ✨ Features

- Checks password length
- Checks for uppercase, lowercase, numbers and special characters
- Detects very common passwords (like `123456` or `password`)
- Gives a score out of 6 and a label: **Weak**, **Medium** or **Strong**
- Suggests how to make the password better
- Hides what you type, and never saves or sends your password anywhere

## 🛠️ Requirements

- Python 3.8 or newer (no extra libraries needed)

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/password-strength-checker.git
   ```
2. Go into the folder:
   ```bash
   cd password-strength-checker
   ```
3. Run the program:
   ```bash
   python password_checker.py
   ```

## 📸 Example Output

```
=== Password Strength Checker ===
(Your typing will be hidden for safety.)

Enter a password to check:

Score    : 4/6
Strength : Medium

How to improve:
  - 12 or more characters is even better.
  - Add special characters like ! @ # $ %.
```

## 📚 What I Learned

- Writing functions and using `if` conditions in Python
- Working with strings and the `string` module
- Basics of what makes a password secure
- Using Git and GitHub

## 🔮 Future Ideas

- Check against a bigger list of leaked passwords
- Add a simple graphical interface (GUI)
- Generate strong random passwords

## 👤 Author

**Bilash Sarkar**
- GitHub: [@YOUR-USERNAME](https://github.com/YOUR-USERNAME)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
