# Explanation

1. **Code Objective and Purpose**

- _Objective:_ To demonstrate core OOP principles: Inheritance, Abstraction, Polymorphism, and Composition.

- _Purpose:_ To provide a structured way to manage different types of library resources, allowing a user to search through a collection and record "checkout" transactions.

2. **Line-by-Line Explanation**

   **Abstraction and Base Class**

- _from abc import ABC, abstractmethod:_ Imports tools to create an Abstract Base Class. You cannot create a generic "Media" object; it must be a specific type (like a Book).

- _class Media(ABC)::_ The parent class for all library items.

- _@abstractmethod:_ This decorator forces any child class (Book/Digital) to create its own get_type method.

- _display_info(self):_ A shared method that all child classes use to print their details.

  **Inheritance (Book & DigitalResource)**

- _class Book(Media)::_ Inherits everything from Media.

- _super().**init**(...):_ Calls the parent class constructor to set the title, author, and ID, then adds self.pages specifically for books.

- _class DigitalResource(Media)::_ Similar to Book, but tracks file_size instead of pages.

  **Logic and Management (Library & Checkout)**

- _class Library::_ Acts as a container. It holds a list (media_collection) and handles the logic for finding items.

- _if keyword.lower() in ...:_ A case-insensitive search that checks both the title and the author's name.

- _class Checkout::_ This uses Composition. It doesn't "inherit" from Media; instead, it "contains" a Media object to link a user to a specific item.

- _datetime.now():_ Automatically records the exact time the checkout occurred.

3. **How the Code Works (The Architecture)**

The code follows a hierarchical structure to ensure data consistency and reusability.

**The Workflow:**

1. _Creation:_ You define specific items (a Book or a DigitalResource).

2. _Storage:_ These items are added to the Library object's list.

3. _Interaction_: \* The search function iterates through the list. Because of Polymorphism, the library doesn't care if an item is a book or a digital file; it just knows they both have titles and authors.

- The **Checkout** class creates a "transaction record" by grouping a User name, a Media object, and a Timestamp.

4. **Key OOP Concepts Used**

| Concept       | Where it appears in the code                                                                     | Example/Notes                                                 |
| ------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Abstraction   | The Media class cannot be instantiated directly.                                                 | Media is likely an abstract base class.                       |
| Inheritance   | Book and DigitalResource get their basic features from Media.                                    | Book and DigitalResource extend Media.                        |
| Polymorphism  | display_info() works on both Books and DigitalResources, even though they are different types.   | A single interface/display method handles multiple types.     |
| Composition   | The Checkout class has a Media object inside it rather than being a type of media itself.        | Checkout uses/holds a Media instance.                         |
| Encapsulation | All data related to a book (pages, author, title) is bundled together within the class instance. | Book encapsulates its own data fields (pages, author, title). |

# UML-Style Structure

Media
├── Book
└── DigitalResource

Library
├── search()
├── add_media()

Checkout
└── Media
