import json

sessions = []
FILE_NAME = "study_log.txt"

def classify_session(duration):
    if duration < 30:
        return "Short"
    elif duration <= 90:
        return "Medium"
    else:
        return "Long"

def get_valid_duration():
    while True:
        try:
            duration = float(input("Enter duration in minutes: "))

            if duration > 0:
                return duration
            else:
                print("Duration must be greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a valid positive number.")


def add_session():
    print("\n--- Add a Study Session ---")

    subject = input("Enter subject name: ").strip()
    topic = input("Enter topic covered: ").strip()
    date = input("Enter date or day: ").strip()
    duration = get_valid_duration()

    session = {
        "subject": subject,
        "topic": topic,
        "date": date,
        "duration": duration
    }

    sessions.append(session)

    classification = classify_session(duration)

    print("\nStudy session added successfully.")
    print(f"Session classification: {classification}")

def view_sessions():
    print("\n--- All Study Sessions ---")

    if not sessions:
        print("No study sessions have been recorded.")
        return

    print("-" * 88)
    print(
        f"{'No.':<5}"
        f"{'Subject':<20}"
        f"{'Topic':<25}"
        f"{'Date/Day':<15}"
        f"{'Minutes':<12}"
        f"{'Class':<10}"
    )
    print("-" * 88)

    for number, session in enumerate(sessions, start=1):
        classification = classify_session(session["duration"])

        print(
            f"{number:<5}"
            f"{session['subject']:<30}"
            f"{session['topic']:<25}"
            f"{session['date']:<15}"
            f"{session['duration']:<12g}"
            f"{classification:<10}"
        )

    print("-" * 88)

def search_by_subject(subject):
    print("\n--- Search Results ---")

    matching_sessions = []

    for session in sessions:
        if session["subject"].lower() == subject.lower():
            matching_sessions.append(session)

    if not matching_sessions:
        print(f"No sessions were found for '{subject}'.")
        return

    print("-" * 98)
    print(
        f"{'No.':<5}"
        f"{'Subject':<20}"
        f"{'Topic':<25}"
        f"{'Date/Day':<15}"
        f"{'Minutes':<12}"
        f"{'Class':<10}"
    )
    print("-" * 98)

    total_minutes = 0

    for number, session in enumerate(matching_sessions, start=1):
        duration = session["duration"]
        classification = classify_session(duration)
        total_minutes += duration

        print(
            f"{number:<5}"
            f"{session['subject']:<30}"
            f"{session['topic']:<25}"
            f"{session['date']:<15}"
            f"{duration:<12g}"
            f"{classification:<10}"
        )

    print("-" * 88)
    print(f"Total time spent on {subject}: {total_minutes:g} minutes")

def study_statistics():
    print("\n--- Study Statistics ---")

    total_minutes = sum(session["duration"] for session in sessions)
    total_hours = total_minutes / 60

    subject_totals = {}

    for session in sessions:
        subject = session["subject"].title()
        duration = session["duration"]

        if subject in subject_totals:
            subject_totals[subject] += duration
        else:
            subject_totals[subject] = duration

    weakest_subject = min(subject_totals, key=subject_totals.get)
    longest_session = max(sessions, key=lambda session: session["duration"])

    print(f"Total hours studied overall: {total_hours:.2f} hours")

    print("\nTotal study time per subject:")

    for subject, minutes in subject_totals.items():
        hours = minutes / 60
        print(f"{subject}: {hours:.2f} hours")

    print(
        f"\nWeakest area: {weakest_subject} "
        f"({subject_totals[weakest_subject] / 60:.2f} hours)"
    )

    print(
        f"Longest session: {longest_session['subject']} - "
        f"{longest_session['topic']} "
        f"({longest_session['duration']:g} minutes)"
    )

def save_sessions():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(sessions, file, indent=4)

        print("Study sessions saved successfully.")

    except OSError:
        print("The study sessions could not be saved.")
    if not sessions:
        print("No study sessions are available for analysis.")
        return

def load_sessions():
    global sessions

    try:
        with open(FILE_NAME, "r") as file:
            sessions = json.load(file)

        print(f"{len(sessions)} saved session(s) loaded successfully.")

    except FileNotFoundError:
        sessions = []
        print("No previous study records found.")

    except json.JSONDecodeError:
        sessions = []
        print("The study log is empty or damaged. Starting with no sessions.")

def display_menu():
    print("\n================================")
    print("       SMART STUDY PLANNER")
    print("================================")
    print("1. Add a study session")
    print("2. View all sessions")
    print("3. Search sessions by subject")
    print("4. View statistics")
    print("5. Save and exit")
    print("================================")

def main():
    load_sessions()

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_session()

        elif choice == "2":
            view_sessions()

        elif choice == "3":
            subject = input("Enter the subject to search for: ").strip()
            search_by_subject(subject)

        elif choice == "4":
            study_statistics()

        elif choice == "5":
            save_sessions()
            print("Thank you for using the Smart Study Planner.")
            break

        else:
            print("Invalid menu choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()