students = {}

while True:
    name = input("Введіть ім'я студента (або 'stop' для завершення): ")
    if name.lower() == "stop":
        break
    grade = int(input(f"Введіть оцінку для {name}: "))
    students[name] = grade

print("\n--- Результати ---")
for name, grade in students.items():
    print(f"{name}: {grade}")

if students:
    avg = sum(students.values()) / len(students)
    print(f"\nСередній бал: {avg:.2f}")

    vidminnyky = [x for x, g in students.items() if 10 <= g <= 12]
    khoroshysty = [x for x, g in students.items() if 7 <= g <= 9]
    vidstayuchi = [x for x, g in students.items() if 4 <= g <= 6]
    ne_sdaly = [x for x, g in students.items() if 1 <= g <= 3]

    print(f"Відмінники ({len(vidminnyky)}): {vidminnyky}")
    print(f"Хорошисти ({len(khoroshysty)}): {khoroshysty}")
    print(f"Відстаючі ({len(vidstayuchi)}): {vidstayuchi}")
    print(f"Не здали ({len(ne_sdaly)}): {ne_sdaly}")