import csv

search_name = input("Enter Student Name: ").strip().lower()

students = []

# Read student records and calculate total marks
with open("student_marks.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["Total"] = (
            int(row["English"])
            + int(row["Maths"])
            + int(row["Physics"])
            + int(row["Chemistry"])
            + int(row["Biology"])
        )

        students.append(row)

# Sort students by total marks in descending order
students_sorted = sorted(
    students,
    key=lambda student: student["Total"],
    reverse=True
)

# Assign class rank
for rank, student in enumerate(students_sorted, start=1):
    student["Rank"] = rank

# Search for the requested student
found = False

for student in students_sorted:
    if student["Student Name"].strip().lower() == search_name:
        found = True

        name = student["Student Name"]
        english = int(student["English"])
        maths = int(student["Maths"])
        physics = int(student["Physics"])
        chemistry = int(student["Chemistry"])
        biology = int(student["Biology"])

        total = student["Total"]
        percentage = (total / 500) * 100
        rank = student["Rank"]

        failed_subjects = [
            subject
            for subject, marks in [
                ("English", english),
                ("Maths", maths),
                ("Physics", physics),
                ("Chemistry", chemistry),
                ("Biology", biology),
            ]
            if marks < 33
        ]

        print("\n" + "=" * 40)
        print(f"          REPORT CARD: {name.upper()}")
        print("=" * 40)

        print(f"  English   : {english}/100")
        print(f"  Maths     : {maths}/100")
        print(f"  Physics   : {physics}/100")
        print(f"  Chemistry : {chemistry}/100")
        print(f"  Biology   : {biology}/100")

        print("-" * 40)

        print(f"  Total     : {total}/500")
        print(f"  Percentage: {percentage:.2f}%")
        print(f"  Class Rank: {rank} out of {len(students)}")

        print("-" * 40)

        if failed_subjects:
            print("  Result    : FAILED THE EXAM")
            print(f"  Failed in : {', '.join(failed_subjects)}")
        else:
            print("  Result    : PASSED THE EXAM")

            if total >= 450:
                print("  Grade     : Grade A+")
            elif total >= 400:
                print("  Grade     : Grade A")
            elif total >= 325:
                print("  Grade     : Grade B")
            elif total >= 250:
                print("  Grade     : Grade C")
            elif total >= 165:
                print("  Grade     : Grade D")
            else:
                print("  Grade     : Grade E")

        print("=" * 40)

        break

if not found:
    print("\nNo record found for this name. Please check the spelling.")