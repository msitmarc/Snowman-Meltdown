# Snowman Meltdown

Ein Hangman-Spiel im Terminal: Statt eines Galgens schmilzt bei jedem falschen
Buchstaben ein Schneemann ein Stück weiter. Codio-Aufgabe zum Üben von Git/GitHub.

## Spielen

```bash
python snowman.py
```

Buchstabe raten, bis das Wort komplett erraten ist oder der Schneemann
vollständig geschmolzen ist. Nach dem Spiel kann man direkt noch eine Runde
starten.

## Dateien

| Datei | Inhalt |
|---|---|
| `snowman.py` | Einstiegspunkt, startet das Spiel |
| `game_logic.py` | Spiellogik (Wortauswahl, Rateschleife, Anzeige) |
| `ascii_art.py` | ASCII-Art-Phasen des schmelzenden Schneemanns |
