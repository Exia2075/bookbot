📚 BookBot

BookBot is a Python command-line program that analyzes the contents of books. It counts the total number of words, calculates the frequency of each character (ignoring case), and prints a sorted report of the most common alphabetical characters.

This project was completed as part of Boot.dev’s Python course and demonstrates file handling, string manipulation, dictionaries, sorting, and CLI programming in Python. 🚀

---

✨ Features

- 📝 Count the total number of words in any text file.

- 🔠 Count the occurrence of each character (case-insensitive).

- 📊 Display the top alphabetical characters in descending order of frequency.

- 💻 Accepts any text file path as a command-line argument.

- ⚡ Fully CLI-based with usage instructions.

---

🚀 Usage

- python3 main.py <path_to_book>

---

🗂 Project Structure

bookbot/
│
├── books/                     # Text files for analysis
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
│
├── main.py                     # Entry point for BookBot
├── stats.py                    # Helper functions for word and character counts
└── README.md                   # Project documentation

---

📊 Example Output

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
============= END ===============

---

🧑‍💻 Author

Exia2075

GitHub: https://github.com/Exia2075/bookbot
