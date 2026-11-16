from pathlib import Path


logs = [
    "2026-10-20 10:00:01 - SUCCESS LOGIN - IP: 10.0.0.12;",
    "2026-10-20 10:00:05 - FAILED LOGIN - IP: 192.168.1.50;",
    "2026-10-20 10:00:07 - FAILED LOGIN - IP: 192.168.1.50;",
    "2026-10-20 10:00:09 - SUCCESS LOGIN - IP: 10.0.0.15;",
    "2026-10-20 10:00:12 - FAILED LOGIN - IP: 192.168.1.50;",
    "2026-10-20 10:00:15 - FAILED LOGIN - IP: 192.168.1.50;",
    "2026-10-20 10:00:18 - FAILED LOGIN - IP: 192.168.1.50;",
    "2026-10-20 10:00:20 - FAILED LOGIN - IP: 172.16.0.4;",
]


def create_log_file(file_path: str = "server.log") -> None:
    Path(file_path).write_text(
        "\n".join(logs) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    create_log_file()

