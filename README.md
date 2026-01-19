# Python Systems Design Checklist Projects – Professional Thinking Guide

This repository is a **curated collection of backend-focused Python checklist projects**, designed to help you **think like a professional Python developer**, not just write working code.

Each project targets a **core software engineering concept** that appears repeatedly in real-world systems, interviews, and production codebases.

The goal is not memorization, but **learning how to approach problems**, **how to decompose systems**, and **how to design clean, scalable solutions**.

---

## How to Use This Repository

For each project:

1. **Read the problem statement**
2. **Understand the core engineering concept**
3. **Apply the thinking hints**
4. **Design before coding**
5. **Implement with clean abstractions**

Think in terms of:

- Responsibility separation
- Scalability
- Testability
- Maintainability

---

## 1. Task Automator – Downloads Folder Organizer

### Problem Statement

Organize files in the Downloads folder by extension and log every action.

### Core Concepts

- File system operations
- Automation scripts
- Logging for observability

### How to Think Like a Professional

- Ask: _What can change?_ (file types, folder paths)
- Avoid hardcoding logic into one function
- Add logging to understand behavior after execution
- Think in terms of **idempotent operations** (safe to re-run)

### Mental Model

> “Automation scripts should be safe, repeatable, and transparent.”

---

## 2. Library Management System (OOP Design)

### Problem Statement

Design a system with a base `Media` class, inherited resources, search functionality, and a checkout system using composition.

### Core Concepts

- Inheritance vs Composition
- Abstraction and polymorphism
- Interface-driven design

### How to Think Like a Professional

- Identify **what varies** (Book vs DigitalResource)
- Identify **what stays stable** (search, checkout)
- Prefer composition for behavior that _uses_ objects
- Use abstract base classes to enforce contracts

### Mental Model

> “Model the real world, not just the data.”

---

## 3. Log Analyzer – Generator + Decorator

### Problem Statement

Measure execution time and process massive CSV files without exhausting RAM.

### Core Concepts

- Decorators
- Generators
- Memory-efficient data processing

### How to Think Like a Professional

- Never load large datasets unless required
- Separate **cross-cutting concerns** (timing, logging) from logic
- Use lazy evaluation for scalability
- Measure performance instead of guessing

### Mental Model

> “Performance problems are architectural problems.”

---

## 4. Asynchronous Weather Scraper

### Problem Statement

Fetch weather data from multiple cities simultaneously and store results using a custom context manager.

### Core Concepts

- Async I/O with `asyncio`
- Non-blocking HTTP requests
- Resource management via context managers

### How to Think Like a Professional

- Ask: _Is this I/O-bound or CPU-bound?_
- Use concurrency where waiting dominates
- Always clean up external resources (DB, network)
- Separate fetching, orchestration, and persistence

### Mental Model

> “Concurrency is about waiting less, not working more.”

---

## 5. Authenticated API Client (GitHub API)

### Problem Statement

Build an authenticated API client with strong typing, logging, and high test coverage.

### Core Concepts

- API client design
- Dependency isolation
- Testing with mocks
- Structured logging

### How to Think Like a Professional

- Assume APIs will fail
- Never mix networking logic with business logic
- Design for testability from day one
- Use explicit exceptions, not silent failures

### Mental Model

> “If it’s not testable, it’s not production-ready.”

---

## 6. E-commerce Backend Core – Dependency Injection

### Problem Statement

Process orders while allowing notification mechanisms (Email/SMS) to be switched without changing order logic.

### Core Concepts

- Dependency Injection (DI)
- SOLID principles
- Loose coupling

### How to Think Like a Professional

- Depend on **abstractions**, not implementations
- Push infrastructure decisions to the edges
- Make systems open for extension, closed for modification
- Design for change before change arrives

### Mental Model

> “Business logic should not care about infrastructure.”

---

## Overall Professional Thinking Pattern

When approaching **any Python backend problem**, ask:

1. What is the **core responsibility**?
2. What parts will **change over time**?
3. Where should **dependencies be injected**?
4. How will this be **tested**?
5. How will failures be **observed and logged**?

---

## Skills This Repository Builds

- System design thinking
- Clean Python architecture
- SOLID principles
- Async & performance awareness
- Real-world test strategies

---

## Final Note

This repository is not about showing off code.

It is about building the **mental habits of a professional Python developer**:

- Design first
- Code second
- Test always
- Think in systems

If you can explain _why_ each design choice exists, you are already ahead of most developers.

---
