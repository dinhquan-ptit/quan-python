# bài toán tính điểm trung bình cao nhất của học sinh
students = [
    {"name": "An", "math": 8, "english": 7, "physics": 9},
    {"name": "Bình", "math": 9, "english": 6, "physics": 7},
    {"name": "Chi", "math": 7, "english": 8, "physics": 8},
    {"name": "Dũng", "math": 6, "english": 7, "physics": 5},
    {"name": "Hà", "math": 9, "english": 9, "physics": 10},
    {"name": "Khánh", "math": 8, "english": 8, "physics": 7},
    {"name": "Linh", "math": 10, "english": 9, "physics": 9},
    {"name": "Minh", "math": 7, "english": 6, "physics": 6},
    {"name": "Nga", "math": 8, "english": 10, "physics": 8},
    {"name": "Quân", "math": 6, "english": 5, "physics": 6},
]
highest_avg = 0
top_student = ""
for student in students:
    tbm = (student["math"] + student["english"] + student["physics"]) / 3
    if tbm > highest_avg:
        highest_avg = tbm
        top_student = student["name"]
print(f"Học sinh có điểm trung bình cao nhất là {top_student} với điểm trung bình {highest_avg:.2f}")
