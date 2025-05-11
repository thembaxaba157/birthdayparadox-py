# 🎂 Birthday Paradox Simulator

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

> Simulate the famous Birthday Paradox and explore probability through Monte Carlo experiments — all in the terminal.

---

## 📸 Demo

### 📍 Sample CLI Output

```
How many birthdays shall I generate? (Max 100)
 > 23

Here are 23 birthdays:
Jul 08, Feb 14, Oct 30, Dec 06, Jul 08, Apr 01, ...

In this simulation, multiple people have a birthday on Jul 08

Generating 23 random birthdays 100,000 times...
0 simulations run...
10000 simulations run...
...
100000 simulations run...

Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50705 times.
This means 23 people have a 50.705% chance of
having a matching birthday in their group.
That's probably more than you would think!
```

---

## 🧠 About the Birthday Paradox

The **Birthday Paradox** (or *Birthday Problem*) is the surprisingly high probability that, in a group of people, **two or more will share the same birthday**.

- In a group of 23 people: **~50%** chance
- In a group of 70 people: **~99.9%** chance

This script performs multiple randomized trials to estimate these probabilities using **Monte Carlo simulation**.

🔗 [Learn more on Wikipedia](https://en.wikipedia.org/wiki/Birthday_problem)

---

## 📦 Features

- 🚀 Fast Monte Carlo simulation (100,000 runs)
- 👤 Input-based simulation size (1–100)
- 📆 Random date generation within 2020
- 🧮 Group probability calculation
- 💻 Interactive terminal experience

---

## 🗂 Project Structure

```text
birthdayparadox-py/
├── birthday_paradox.py    # Main script
├── README.md              # Project documentation
```

---

## 🛠️ Requirements

- Python 3.8 or newer

No external dependencies are required. Uses built-in modules:
- `random`
- `datetime`
- `getpass`
- `statistics`

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/thembaxaba157/birthdayparadox-py.git
   cd birthdayparadox-py
   ```

2. Run the script:
   ```bash
   python3 birthday_paradox.py
   ```

3. Follow prompts in the terminal.

---

## 🔬 How It Works

- You enter the number of people to simulate.
- The program generates that many random birthdays (in the year 2020).
- It shows a sample group and whether duplicates exist.
- Then it simulates **100,000 random groups** of that size.
- It calculates how often at least one shared birthday occurs.

This is a **Monte Carlo experiment** — repeating random trials to estimate a real-world probability.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙋‍♂️ Author

Created by [@thembaxaba157](https://github.com/thembaxaba157) — inspired by [Al Sweigart](https://inventwithpython.com/).

---

## ⭐️ Star the repo if you find it useful or educational!

