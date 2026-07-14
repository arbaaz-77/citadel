# 🏰 Citadel Archive

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/status-in%20development-green)
![License](https://img.shields.io/badge/license-MIT-blue)

A command-line Python application inspired by the **Game of Thrones** and **A Song of Ice and Fire** universe.

The Citadel Archive allows users to manage a collection of Game of Thrones characters by viewing, searching, adding, removing, saving, and loading records.
The project began as a procedural Python application and has since evolved into an object-oriented codebase to demonstrate clean software design, modular architecture, and modern Git workflows.

---

## ✨ Features

- View all characters in the archive
- Search for characters by name
- Add new characters
- Prevent duplicate character entries
- Remove existing characters
- Save the archive to a JSON file
- Load the archive from a JSON file
- Automatic validation of character objects
- Case-insensitive searching
- Shared House objects using object composition

---

## 🏗️ Project Structure

```text
citadel/
│
├── archive.py          # Archive management and JSON persistence
├── character.py        # Character model
├── house.py            # House model
├── citadel.py          # Menu, input handling and application entry point
├── characters.json     # Persistent character data
├── README.md
└── .gitignore
```

---

## 🧠 Software Engineering Concepts Demonstrated

### Object-Oriented Programming (OOP)

- Classes and objects
- Constructors (`__init__`)
- Instance methods
- Class methods (`@classmethod`)
- Encapsulation
- Separation of responsibilities

### Data Serialization

- Convert Python objects to dictionaries
- Save data using JSON
- Load JSON back into Python objects
- Persistent application state

### Clean Architecture

- `Character` is responsible for representing a character.
- `Archive` is responsible for managing the collection of characters.
- User input is separated from business logic.
- `main()` controls the application flow.
- House represents a shared domain object used by multiple characters.

### Python Concepts

- Classes
- Functions
- Lists
- Loops
- Conditionals
- Modules
- File I/O
- JSON
- Error handling
- 
- Object composition
- Serialization
- Shared object registries

---

## 🏛️ Architecture

The project is organized into small, focused modules.

```text
citadel.py
    │
    ▼
archive.py
    │
    ▼
character.py
    │
    ▼
house.py
```
---

## 💾 Example Character

```text
Name: Jon Snow
House: Stark
Title: King in the North
```

---

## 🚀 Running the Project

Clone the repository:

```bash
git clone https://github.com/arbaaz-77/citadel.git
```

Navigate into the project:

```bash
cd citadel
```

Run the application:

```bash
python citadel.py
```

---

## 🛠️ Git Workflow Used

This project is developed using a feature branch workflow.

- Create a feature branch
- Make focused commits
- Push to GitHub
- Open a Pull Request
- Review changes
- Merge into `main`

Example commit messages:

```text
feat: serialize Character objects to JSON
refactor: migrate archive operations to objects
docs: update README for OOP refactor
```

---

## 🎯 Future Improvements

- Add unit tests using `pytest`
- Introduce type hints throughout the project
- Add character editing functionality
- Store additional character attributes (weapon, allegiance, status)
- Add filtering and sorting
- Build a graphical interface
- Expose the archive through a REST API
- Integrate an AI assistant to answer questions about the archive

---

## 📚 Learning Goals

This project is part of my journey from **QA Engineer** to **AI Developer**.

The focus is not only on learning Python syntax, but also on building strong software engineering fundamentals, including:

- Clean code
- Object-oriented design
- Refactoring
- Git and GitHub workflows
- Project organization
- Building the software engineering foundation required for AI application development.

---

## ⚔️ Inspiration

> "The man who passes the sentence should swing the sword."

— Eddard Stark

Built with Python, curiosity, and many late nights in the Citadel.
