#!/usr/bin/env zsh

# Funktion zum Aktivieren der virtuellen Umgebung
activate_venv() {
    source venv/bin/activate
    hash -r # Zsh: Befehls-Cache zurücksetzen
    export PATH="$(pwd)/venv/bin:$PATH"
}

# Prüfen, ob venv existiert
if [[ ! -d "venv" || ! -f "venv/bin/activate" ]]; then
    echo "Virtuelle Umgebung wird erstellt..."
    python3 -m venv venv
    activate_venv
    echo "Installiere Abhängigkeiten aus requirements.txt..."
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "Aktiviere bestehende virtuelle Umgebung..."
    activate_venv
fi

echo "Python verwendet: $(which python)"
invoke -l