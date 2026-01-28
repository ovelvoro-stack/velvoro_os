from app.services.reminder_service import pending_reminders

def run():
    reminders = pending_reminders()
    for r in reminders:
        print("REMINDER:", r)

if __name__ == "__main__":
    run()
