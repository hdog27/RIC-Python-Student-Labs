"""Worked example about session length, separate from the project."""
minutes = int(input("Minutes per session: "))
if minutes > 0:
    print(f"Three sessions take {minutes * 3} minutes.")
else:
    print("Choose a positive duration.")
