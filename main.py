import subprocess
from datetime import datetime

# 1. Make some change so there's something to commit
with open("progress.md", "a") as f:
    f.write(f"- Practiced DSA on {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

# 2. Stage, commit, push
subprocess.run(["git", "add", "progress.md"], check=True)
subprocess.run(["git", "commit", "-m", f"Daily update: {datetime.now().date()}"], check=True)
subprocess.run(["git", "push"], check=True)

print("Pushed. Check your contribution graph in a minute.")
