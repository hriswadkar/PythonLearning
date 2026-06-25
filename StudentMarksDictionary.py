# This program accepts student name and marks from the user and stores them in a dictionary.
# It then displays average marks per student.
# It also finds the top scorer and returns scorer name + score.

def get_student_details() -> dict[str, list[float]]:
    student_marks: dict[str, list[float]] = {}

    while True:
        entry = input(
            "Enter student name and mark(s) as name: mark, name: mark (or 'done' to finish): "
        ).strip()

        if entry.lower() == "done" or entry == "":
            break

        # Support inline trailing "done", e.g. "Akka: 70 done"
        stop_after_this_line = False
        if entry.lower().endswith(" done"):
            entry = entry[:-5].strip()
            stop_after_this_line = True

        if not entry:
            break

        student_entries = entry.split(",")
        for student_entry in student_entries:
            student_entry = student_entry.strip()

            # Support comma-separated done token, e.g. "..., done"
            if student_entry.lower() == "done":
                stop_after_this_line = True
                continue

            if ":" not in student_entry:
                print(f"Skipping invalid entry: {student_entry}")
                continue

            name, marks = student_entry.split(":", 1)
            name = name.strip()

            try:
                mark_value = float(marks.strip())
            except ValueError:
                print(f"Skipping invalid marks for {name}: {marks.strip()}")
                continue

            if name not in student_marks:
                student_marks[name] = []
            student_marks[name].append(mark_value)

        if stop_after_this_line:
            break

    return student_marks


def calculate_average_marks(student_marks: dict[str, list[float]]) -> dict[str, float]:
    average_marks: dict[str, float] = {}
    for name, marks in student_marks.items():
        if marks:
            average_marks[name] = sum(marks) / len(marks)
    return average_marks


def find_top_scorer(average_marks: dict[str, float]) -> tuple[str | None, float]:
    if not average_marks:
        return None, 0.0
    top_scorer = max(average_marks, key=average_marks.get)
    top_score = average_marks[top_scorer]
    return top_scorer, top_score


def main() -> None:
    print("This program calculates average marks per student and finds the top scorer.")
    student_marks = get_student_details()
    average_marks = calculate_average_marks(student_marks)
    top_scorer, top_score = find_top_scorer(average_marks)

    if not average_marks:
        print("No student data available.")
        return

    print("\nAverage marks per student:")
    for name, avg in average_marks.items():
        print(f"{name}: {avg:.2f}")

    print(f"\nTop scorer: {top_scorer} with an average score of {top_score:.2f}")


if __name__ == "__main__":
    main()