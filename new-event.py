#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path
import yaml
from datetime import datetime, timedelta

print("start new event")
if len(sys.argv) != 3:
    print("Usage: python3 create_event.py YYYY-MM-DD event-kind")
    sys.exit(1)

date_str = sys.argv[1]       # Startdatum, z.B. 2026-03-23
event_kind = sys.argv[2]     # z.B. wochenende-merzhausen
file_name = f"content/termine/{date_str}-{event_kind}.md"
file_path = Path(file_name)

# 1️⃣ Datum validieren
try:
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
except ValueError:
    print(f"ERROR: Ungültiges Datum: {date_str}")
    sys.exit(1)

# 2️⃣ Existierende Datei prüfen
if file_path.exists():
    print(f"ERROR: Datei existiert bereits: {file_path}")
    sys.exit(1)

# 3️⃣ Hugo new ausführen
try:
    subprocess.run([
        "hugo", "new", str(file_path),
        "--kind", event_kind
    ], check=True)
except subprocess.CalledProcessError as e:
    print(f"ERROR: Hugo new fehlgeschlagen: {e}")
    sys.exit(1)

# 4️⃣ Datei einlesen und Frontmatter ersetzen
with file_path.open("r", encoding="utf-8") as f:
    content = f.read()

# Frontmatter extrahieren
if content.startswith("---"):
    parts = content.split("---", 2)
    yaml_content = parts[1]
    body_content = parts[2] if len(parts) > 2 else ""
else:
    yaml_content = ""
    body_content = content

data = yaml.safe_load(yaml_content) or {}

# 5️⃣ startDate, endDate, expiryDate setzen
if event_kind in ["gemeindehaus", "schafferei"]:
    # Veranstaltungen von 17:00-22:00 am gleichen Tag
    data["startDate"] = f"{start_date.strftime('%Y-%m-%d')}T17:00:00+01:00"
    data["endDate"] = f"{start_date.strftime('%Y-%m-%d')}T22:00:00+01:00"
    data["expiryDate"] = f"{start_date.strftime('%Y-%m-%d')}T22:00:00+01:00"
    title_suffix = data.get("title", event_kind.replace("-", " ").title())
    data["title"] = f"{start_date.strftime('%d.%m.%Y')}: {title_suffix}"
else:
    # Mehrtagesevent (Wochenende)
    end_date = start_date + timedelta(days=1)
    data["startDate"] = f"{start_date.strftime('%Y-%m-%d')}T00:00:00+01:00"
    data["endDate"] = f"{end_date.strftime('%Y-%m-%d')}T23:59:59+01:00"
    data["expiryDate"] = f"{end_date.strftime('%Y-%m-%d')}T23:59:59+01:00"
    title_suffix = data.get("title", event_kind.replace("-", " ").title())
    data["title"] = f"{start_date.strftime('%d.%m.%Y')}: {title_suffix}"


# 8️⃣ YAML zurückschreiben
with file_path.open("w", encoding="utf-8") as f:
    f.write("---\n")
    yaml.dump(data, f, sort_keys=False, allow_unicode=True)
    f.write("---\n")
    f.write(body_content.lstrip())

print(f"Event-Datei erstellt: {file_path}")
