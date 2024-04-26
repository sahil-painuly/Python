from datetime import datetime

now = datetime.now()

hour = now.hour
minute = now.minute
second = now.second

if hour == 24 or (hour >= 1 and hour <= 11):
    greeting = "Good Morning Sir!"
elif hour >= 12 and hour <= 16:
    greeting = "Good Afternoon Sir!"
elif hour >= 17 and hour <= 23:
    greeting = "Good Evening Sir!"


if hour > 12:
    hour -= 12

print(f"{greeting} Present time: {hour:02d}:{minute:02d}:{second:02d}")
