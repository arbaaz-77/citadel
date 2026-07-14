# 🏰 Citadel Archive v2.0

A command-line Python application inspired by the **Game of Thrones** and **A Song of Ice and Fire** universe.

The Citadel Archive allows users to manage a collection of characters by viewing, searching, adding, removing, saving, and loading records. While it began as a procedural Python project, Version 2.0 has been fully refactored into an object-oriented application to demonstrate clean software design and modern development practices.

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

---

## 🏗️ Project Structure

```text
citadel/
│
├── archive.py          # Archive management and JSON persistence
├── character.py        # Character model
├── citadel.py          # Archive, menu, and application entry point
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

### Python Concepts

- Classes
- Lists
- Loops
- Conditionals
- Functions
- Error handling
- File I/O
- JSON
- Modules and imports

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
- Manage Houses as their own objects
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
- Preparing for AI application development

---

## ⚔️ Inspiration

> "The man who passes the sentence should swing the sword."

— Eddard Stark

Built with Python, curiosity, and many late nights in the Citadel.
