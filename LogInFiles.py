import re
from collections import Counter
from ipaddress import ip_address
from pathlib import Path


IP_PATTERN = re.compile(r"IP:\s*(\S+)")


def analyze_log(file_path: str | Path, threshold: int = 3) -> Counter[str]:
    failed_attempts: Counter[str] = Counter()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if "FAILED LOGIN" not in line:
                    continue

                match = IP_PATTERN.search(line)
                if not match:
                    continue

                ip = match.group(1).rstrip(";")

                try:
                    ip_address(ip)
                except ValueError:
                    continue

                failed_attempts[ip] += 1

    except FileNotFoundError:
        print(f"Filen blev ikke fundet: {file_path}")
        return failed_attempts

    print("--- Analyzing Logs ---")

    for ip, count in failed_attempts.items():
        if count >= threshold:
            print(
                f"[WARNING] Potential brute-force attack from IP: "
                f"{ip} ({count} failed attempts)"
            )
        else:
            print(f"[INFO] Minor failed attempts from IP: {ip} ({count})")

    return failed_attempts


if __name__ == "__main__":
    analyze_log("server.log", threshold=3)