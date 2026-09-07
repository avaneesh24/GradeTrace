# GradeTracer

A beginner-friendly Python project that reads student marks from a CSV file and generates report cards.

---

🎯 Features

The program generates:

- Marks in five subjects
- Total and percentage
- Class rank
- Failed subjects
- Grade
- Pass/fail status

---

⚙️ How It Works

CSV file → Read records → Calculate totals → Rank students → Generate report

---

🛠️ Technologies

- Python 3
- CSV
- File handling
- Dictionaries and lists
- Loops and conditionals
- Sorting and list comprehensions
- f-strings

---

📁 Project Structure

student-marks-analyzer/
├── student_marks.py
├── student_marks.csv
└── README.md

---

▶️ Running the Project

git clone <your-repository-url>
cd student-marks-analyzer
python student_marks.py

Enter a student's name when prompted.

---

🧾 Sample Output

========================================
          REPORT CARD: SAISHA KAUSHIK
========================================
  English   : 43/100
  Maths     : 37/100
  Physics   : 41/100
  Chemistry : 35/100
  Biology   : 39/100
----------------------------------------
  Total     : 195/500
  Percentage: 39.00%
  Class Rank: 45 out of 50
----------------------------------------
  Result    : PASSED THE EXAM
  Grade     : Grade D
========================================
---

🧠 What I Learned

This project helped me practice:

- Reading and processing CSV data
- Converting strings to numbers
- Calculating totals and percentages
- Sorting and searching records
- Creating grades and result logic
- Formatting readable output

---

🔎 Limitations

- Requires valid numerical marks
- Uses student names for searching
- Gives sequential ranks for ties
- Supports five fixed subjects
- Has no graphical interface

---

🚀 Future Improvements

- Input validation
- Tie-aware ranking
- Student record management
- Class statistics
- Data visualization
- SQLite integration
- GUI or web interface

---

📌 About the Project

This is one of my early projects as a first-year engineering student. I built it to practice combining Python fundamentals into a useful application.

---

👨‍💻 About Me

I'm exploring Python, AI/ML while improving my programming fundamentals through practical projects.

⭐ Feel free to explore the repository.
