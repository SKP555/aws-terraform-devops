import subprocess
import re

print("🔍 AI Log Analyzer Started...\n")

# Read Docker logs
logs = subprocess.getoutput("docker logs sonu-container")

# Error patterns
error_patterns = [
    "error",
    "failed",
    "exception",
    "timeout",
    "critical"
]

found_issues = []

# Scan logs
for pattern in error_patterns:
    matches = re.findall(pattern, logs, re.IGNORECASE)

    if matches:
        found_issues.append(pattern)

# AI-style analysis
if found_issues:
    print("⚠ Potential issues detected:\n")

    for issue in found_issues:
        print(f"- Detected keyword: {issue}")

    print("\n🤖 AI Self-Healing Triggered...")
    print("Restarting container...\n")

    # Restart container
    restart = subprocess.getoutput("docker restart sonu-container")

    print(f"✅ Container restarted successfully: {restart}")

else:
    print("✅ No critical issues detected.")
