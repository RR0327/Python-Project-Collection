# Python Systems Design Checklist Projects

This repository contains a curated set of **Python practice projects** designed to strengthen **core software engineering thinking**, not just syntax.

Each project focuses on a **specific mindset**: how to break down the problem, how to choose the right tools, and how to design a clean solution.

> **Important:**
> These projects were originally provided as _practice challenges_.
> I have personally completed all of them and collected them here as a **learning-focused portfolio**, not copy-paste solutions.

---

## Table of Contents

1. [Task Automator – Downloads Organizer](#1-task-automator--downloads-organizer)
2. [Library Management System (OOP)](#2-library-management-system-oop)
3. [Log Analyzer – Decorator & Generator](#3-log-analyzer--decorator--generator)
4. [Asynchronous Weather Scraper](#4-asynchronous-weather-scraper)
5. [E-commerce Backend Core (Dependency Injection)](#5-e-commerce-backend-core-dependency-injection)
6. [What This Repository Trains You For](#what-this-repository-trains-you-for)
7. [Suggested Extensions](#suggested-extensions)

---

## 1. Task Automator – Downloads Organizer

### Problem Thinking

Before writing any code, ask yourself:

- What **repetitive manual task** am I automating?
- What information decides _where a file should go_?
- What should happen **every time** the script runs?

### How to Think About the Solution

- Think in terms of **rules**, not files
  → “If extension is `.pdf`, it belongs to PDFs.”
- Break the task into **small responsibilities**:
  - Detect files
  - Identify type
  - Move safely
  - Log actions

- Assume the script may run multiple times
  → Avoid errors if folders already exist

### Key Hint

> Treat the filesystem like a dataset.
> Each file is just a record with attributes (name, extension, path).

---

## 2. Library Management System (OOP)

### Problem Thinking

This is **not** about storing books.
It is about modeling **real-world entities** in code.

Ask yourself:

- What properties are **shared** by all library items?
- What behavior is **common**, and what is **specific**?

### How to Think About the Solution

- Start with the **most general concept**
  → “Media” before “Book”
- Use inheritance **only when there is a clear ‘is-a’ relationship**
- Avoid putting everything in one class
  → Searching, storage, and checkout are **different responsibilities**
- Composition answers the question:
  → “Who uses whom?”

### Key Hint

> If you struggle to explain a class in one sentence, it probably does too much.

---

## 3. Log Analyzer – Decorator & Generator

### Problem Thinking

This project is about **scale**, not correctness.

Ask yourself:

- What happens if the file is **huge**?
- Do I really need _everything_ in memory at once?
- What behavior should be **reusable** across functions?

### How to Think About the Solution

- Separate **what a function does** from **how it is monitored**
- Use generators when:
  - Data is large
  - Processing is sequential

- Think of decorators as:
  → “Features added _around_ a function, not inside it”

### Key Hint

> If your program crashes on large input, the logic might be right—but the **thinking is wrong**.

---

## 4. Asynchronous Weather Scraper

### Problem Thinking

This is about **waiting efficiently**.

Ask yourself:

- Am I CPU-bound or waiting on the network?
- Why wait for one response when I can wait for many?

### How to Think About the Solution

- Think in **tasks**, not steps
- Networking is I/O-bound
  → Async is about **overlapping waiting time**
- Separate responsibilities:
  - Fetching data
  - Coordinating tasks
  - Saving results

- Context managers answer:
  → “Who cleans up resources if something goes wrong?”

### Key Hint

> Async code is not about speed—it is about **not being idle**.

---

## 5. E-commerce Backend Core (Dependency Injection)

### Problem Thinking

This project is about **change**, not features.

Ask yourself:

- What is most likely to change in the future?
- What should stay stable no matter what?

### How to Think About the Solution

- Business logic should **not care** about implementation details
- Depend on **abstractions**, not concrete classes
- Inject dependencies from the outside
  → Do not create them internally
- Design so that:
  - Adding a new feature requires **adding**, not modifying

### Key Hint

> Good design is when change feels boring instead of risky.

---

## What This Repository Trains You For

This collection strengthens:

- Problem decomposition
- Object-oriented design thinking
- Memory-efficient data processing
- Asynchronous programming mindset
- SOLID principles & clean architecture
- Writing testable, maintainable code

These are **interview-grade fundamentals**, not toy exercises.

---

## Suggested Extensions

If you want to go further:

- Add `pytest` tests for each project
- Generate coverage reports
- Add structured logging
- Package projects as installable modules
- Write system-level diagrams

---

## Final Note

This repository is intentionally **thinking-first**.

If you can explain _why_ each design choice exists,
you are no longer just practicing Python—you are practicing **software engineering**.

---

> If you find this useful, feel free to fork, extend, and experiment.

# Author

Built by **Md Rakibul Hassan**

CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast

[LinkedIn](https://www.linkedin.com/in/mdrakibulhassanmiyaji)

[GitHub](https://github.com/RR0327/)
