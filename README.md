# BMI Calculator 🧮

A simple Python program that calculates a person's **Body Mass Index (BMI)** using their weight and height, then classifies the result into a BMI category.

## 📌 Features

* Takes **weight in kilograms (kg)** as input.

* Takes **height in meters (m)** as input.

* Calculates BMI using the formula:

  **BMI = weight / height²**

* Displays BMI rounded to **1 decimal place**.

* Classifies BMI into:

  * **Underweight:** BMI < 18.5
  * **Normal:** BMI < 25
  * **Overweight:** BMI < 30
  * **Obese:** BMI ≥ 30

## 🛠️ Requirements

* Python 3.x

No external libraries are required.

## ▶️ How to Run

1. Make sure Python is installed.
2. Open a terminal in the project folder.
3. Run:

```bash
python bmi.py
```

4. Enter your weight and height when prompted.

## 💻 Example

```text
Enter your weight (kg): 70
Enter your height (m): 1.75

BMI: 22.9
Category: Normal
```

## 📂 File Structure

```text
.
├── bmi.py
└── README.md
```

## 📚 What I Learned

This project demonstrates basic Python concepts such as:

* `input()` for taking user input
* `float()` for converting input to numbers
* Arithmetic calculations
* `if`, `elif`, and `else` statements
* f-strings for formatted output

## 👨‍💻 Author

Asad Bashir
