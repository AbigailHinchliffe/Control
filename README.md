# Control

A small Risk-like strategy game where three teams (Player, Neutral, AI) compete to control territories. The game cycles through Fortify, Attack and Defend phases.

---

## 1. Project Title and Description
- Project: Control
- Description: Turn-based territory control game with troop placement, dice-based combat, and card mechanics.
- Key features:
  - Fortify, Attack and Defend phases
  - Territory adjacency and troop transfers
  - Card rewards and hand-ins for extra troops
  - AI opponent and neutral territories

## 2. Installation and Setup Instructions

Prerequisites:
- Windows (tested)
- Python 3.8+ installed
- pip available

Clone the repository:
```bash
git clone https://github.com/AbigailHinchliffe/Control.git
```

Install dependencies (pygame required):
```powershell
# Windows PowerShell
py -3 -m pip install pygame
# or if using a venv:
.\venv\Scripts\activate
python -m pip install pygame
```

Run the project:
```powershell
py -3 NEA_main_project.py
# or
python NEA_main_project.py
```

Tip: In VS Code, select the interpreter that has pygame installed (Command Palette → Python: Select Interpreter).

## 3. Usage Instructions
- Start the game and follow on-screen prompts.
- Fortify phase: place troops and optionally trade cards.
- Attack phase: select attacker and defender territories, choose troop allocation, resolve combat with dice.
- Defend (Fortify/Transfer) phase: transfer troops between adjacent owned territories (one transfer per defend phase).
- Use arrow/plus-minus UI to change troop counts.
- Screenshots/GIFs: add to /images or /docs and reference here for visual guidance.

## 4. Project Structure and Technologies Used (Optional)
- Files:
  - NEA_main_project.py — main game loop and setup
  - Classes/classes.py — game classes (Territory, MenuButton, Cards, etc.)
  - Images/ — assets used by the game
  - README.md — this file
- Technologies:
  - Python, pygame
- Development tools:
  - Visual Studio Code

## 5. Known Issues or Limitations (Optional)
- VS Code may show "pygame not found" if the selected interpreter doesn't have pygame installed; ensure the correct interpreter is selected.
- Large images may impact performance on lower-end machines.
- AI behavior and balancing may need improvements.

## 6. Contribution Guidelines (Optional)
- Fork → create a feature branch → submit PR.
- Keep changes focused and add tests where applicable.

## 7. Contact Information
- Author: Abigail Hinchliffe
- GitHub: https://github.com/AbigailHinchliffe
