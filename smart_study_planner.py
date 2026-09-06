
sessions = []

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
            f"{session['subject']:<20}"
            f"{session['topic']:<25}"
            f"{session['date']:<15}"
            f"{session['duration']:<12g}"
            f"{classification:<10}"
        )

    print("-" * 88)