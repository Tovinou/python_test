# Testdokumentation – Timer & Note Widget App

## Översikt
Denna dokumentation beskriver user stories, acceptanskriterier, testscenarier och automatiserade end-to-end tester för projektet. Fokus ligger på funktionalitet för timers, anteckningar, widgets och temahantering.

Applikation: `https://tovinou.github.io/test/`  
Kodbas: `https://github.com/Tovinou/test.git`  
Status: ✅ Deployad och fungerar

---

## 1. USER STORIES

# Skapa timer
# Scenario: Användaren skapar en timer-widget
  Given att appen är öppen
  When användaren klickar på "Add timer"
  Then ska en ny timer-widget visas i listan av widgets

# Skapa anteckning
# Scenario: Användaren skapar en antecknings-widget
  Given att appen är öppen
  When användaren klickar på "Add note"
  Then ska en antecknings-widget visas i listan av widgets

# Ta bort widget
# Scenario: Användaren tar bort en widget
  Given att det finns minst en widget
  When användaren klickar på widgetens "Remove"-knapp
  Then ska widgeten tas bort från vyn

# Byta plats på widgets
#Scenario: Användaren byter plats på två widgets
  Given att det finns minst två widgets
  When användaren drar en widget till en annan widgets position
  Then ska deras placering bytas

# Timerfunktioner
# Ändra tidsinställning
# Scenario: Användaren ändrar timerinställningen
  Given att en timer-widget finns
  When användaren öppnar inställningar och ändrar värdet
  Then ska timern visa den nya starttiden

# Starta timer
# Scenario: Användaren startar timern
  Given att en timer-widget finns
  And timern står på startvärdet
  When användaren klickar på "Start"
  Then ska timern börja räkna ner

# Pausa timer
# Scenario: Användaren pausar timern
  Given att en timer räknar ner
  When användaren klickar på "Pause"
  Then ska nedräkningen stanna men inte återställas

# Återställa timer
# Scenario: Användaren återställer timern
  Given att en timer körs eller är pausad
  When användaren klickar på "Reset"
  Then ska timern återgå till utgångstiden och sluta räkna

# Anteckningar
# Ändra text
Scenario: Användaren redigerar text i en antecknings-widget
  Given att en antecknings-widget finns
  When användaren klickar på textområdet och skriver ny text
  Then ska widgetens text uppdateras

# Ändra temafärg
# Scenario: Användaren byter tema
  Given att appen är öppen
  When användaren klickar på en temaknapp (ex. "Dark", "Forest", "Light")
  Then ska appens färgschema ändras till valt tema
---

## 2. ACCEPTANSKRITERIER

A-

### Skapa timer
| Kriterium | Beskrivning |
|-----------|-------------|
| UI-knapp | En knapp "Add timer" ska finnas |
| Ny widget skapas | När knappen klickas skapas en timer |
| Standardtid | Timer startar med defaultvärde, t.ex. 15:00 |

### Skapa anteckning
| Kriterium | Beskrivning |
|-----------|-------------|
| UI-knapp | En knapp "Add note" ska finnas |
| Ny widget skapas | När knappen klickas visas en anteckning |
| Defaulttext | Standardtext visas tills användaren ändrar den |

### Ta bort widget
| Kriterium | Beskrivning |
|-----------|-------------|
| UI-knapp | Varje widget ska kunna raderas |
| Effekt | Widget tas bort från visningen |

B-

### Hantera flera widgets
| Kriterium | Beskrivning |
|-----------|-------------|
| Mixed layout | Appen kan visa både timers och notes samtidigt |
| Widget-ordning | Timers renderas först, sedan notes |
| Notera | Drag-and-drop är inte implementerat i nuvarande version |

C-

### Timerfunktioner
| Funktion | Kriterier |
|----------|-----------|
| Start | Timer börjar räkna ner |
| Pause | Timer stoppar utan att återställas |
| Reset | Timer återgår till startvärde |
| Ändra tid | Ny starttid sparas och används vid reset |

D-

### Anteckningsredigering
| Kriterium | Beskrivning |
|-----------|-------------|
| Redigerbart textfält | Text kan ändras |
| Automatiskt sparande | Ändringen visas direkt |

E-

### Ändra tema
| Kriterium | Beskrivning |
|-----------|-------------|
| Tema-knappar | Teman kan väljas |
| UI ändras | Färger uppdateras när tema byts |

---

## 3. TESTSCENARIER (Gherkin)

# 1 — Skapa och radera widgets
# Scenario: Användaren lägger till och tar bort widgets

  Given appen är öppen
  When användaren klickar på "Add timer"
  Then ska en timer-widget visas

  When användaren klickar på "Add note"
  Then ska en antecknings-widget visas

  When användaren tar bort en timer-widget
  Then ska timern inte längre visas

# 2 — Timer start, paus, reset
# Scenario: Styra timer

  Given en timer-widget finns
  When användaren klickar "Start"
  Then ska tiden börja minska

  When användaren klickar "Pause"
  Then ska tiden sluta minska

  When användaren klickar "Reset"
  Then ska tiden återställas till startvärdet

# 3 — Anpassa starttid
# Scenario: Användaren ändrar timerinställning

  Given en timer-widget finns
  When användaren ändrar startvärdet till 10:00
  And klickar "Reset"
  Then ska timerdisplayen visa 10:00

# 4 — Redigera anteckning
# Scenario: Ändra text i anteckning

  Given en anteckning finns
  When användaren skriver ny text
  Then ska widgeten visa den uppdaterade texten

# 5 — Ändra tema
# Scenario: Byta tema

  Given att appen är öppen
  When användaren klickar på "Forest"
  Then ska appens färgtema ändras till Forest