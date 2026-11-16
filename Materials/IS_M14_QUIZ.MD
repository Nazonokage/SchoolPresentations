# Comprehensive Review & Assessment: UML and Database Design

Here is a simplified, three-part review guide and assessment based on the core concepts of UML and Relational Database Design.

---

## Part 1: Lesson Recap & Review

Before taking the quiz, quickly review these key concepts:

*   **UML (Unified Modeling Language):** A standard visual language used to create blueprints for software systems. It is divided into **Structural** (static) and **Behavioral** (dynamic) diagrams.
    *   *Use Case:* Functional requirements and actors.
    *   *Class:* Static structure, attributes, and methods.
    *   *Sequence:* Message passing over time.
    *   *State Machine:* States and transitions of an object.
    *   *Activity:* Flow of control/processes.
    *   *Component:* Physical structure of the system.
    *   *Deployment:* Physical hardware and software mapping.
*   **Relational Database Model:** Organizes data into tables (relations) consisting of rows (records) and columns (attributes), linked by keys.
*   **Keys & Indexing:** 
    *   *Primary Key:* Uniquely identifies a record.
    *   *Foreign Key:* Links to a primary key in another table to establish relationships.
    *   *Indexing:* A data structure (like a book's index) that speeds up data retrieval.
*   **Normalization:** The process of organizing data to minimize redundancy and dependency.
    *   *1NF:* Atomic values, unique rows.
    *   *2NF:* No partial dependencies (must rely on the whole primary key).
    *   *3NF:* No transitive dependencies (non-key columns cannot depend on other non-key columns).
    *   *BCNF:* A stricter version of 3NF.

---

## Part 2: Long Quiz

**Identify or discuss what is being asked in the following questions.** *(Note: The original quiz repeated questions 1-5 as questions 16-20. They have been omitted here for brevity).*

1.  What is UML?
2.  What is a use case diagram?
3.  What is a class diagram?
4.  What is a sequence diagram?
5.  What is a state machine diagram?
6.  What is an activity diagram?
7.  What is a component diagram?
8.  What is a deployment diagram?
9.  What is a relational database model?
10. What are the features of a good relational database design?
11. What are the various normal forms from the first normal form through the Boyce-Codd normal form?
12. What is normalization?
13. What is a primary key?
14. What is a foreign key?
15. What is indexing?

---

## Part 3: Answer Key

1.  **What is UML?**
    **Answer:** Unified Modeling Language is a general-purpose, standard visual modeling language used to specify, visualize, construct, and document the artifacts of software systems.
2.  **What is a use case diagram?**
    **Answer:** A behavioral UML diagram that represents the functional requirements of a system, illustrating the interactions between external actors and the system's use cases.
3.  **What is a class diagram?**
    **Answer:** A structural UML diagram that represents the static structure of a system, showing its classes, attributes, methods, and the relationships between them.
4.  **What is a sequence diagram?**
    **Answer:** A behavioral UML diagram that shows how objects interact with each other over time, focusing on the sequence of messages passed between them.
5.  **What is a state machine diagram?**
    **Answer:** A behavioral UML diagram that illustrates the dynamic behavior of a single object, showing the different states it can be in and the events that trigger transitions between those states.
6.  **What is an activity diagram?**
    **Answer:** A behavioral UML diagram that models the workflow or flow of control within a system, representing the steps of a process.
7.  **What is a component diagram?**
    **Answer:** A structural UML diagram that represents the physical organization of a software system, showing how components (modular parts) are wired together.
8.  **What is a deployment diagram?**
    **Answer:** A structural UML diagram that visualizes the physical deployment of software artifacts onto hardware nodes (like servers or devices).
9.  **What is a relational database model?**
    **Answer:** A database model that organizes data into one or more tables (relations) of rows (records) and columns (attributes), where relationships are established using common keys.
10. **What are the features of a good relational database design?**
    **Answer:** Features include minimal data redundancy, high data integrity (accuracy/consistency), scalability, efficient performance, and clear, logical table structures using primary and foreign keys.
11. **What are the various normal forms from the first normal form through the Boyce-Codd normal form?**
    **Answer:** 
    *   **1NF:** Atomic values, unique rows.
    *   **2NF:** 1NF + no partial dependencies.
    *   **3NF:** 2NF + no transitive dependencies.
    *   **BCNF:** 3NF + every determinant is a candidate key.
12. **What is normalization?**
    **Answer:** The process of organizing data in a database by dividing larger tables into smaller ones and linking them via relationships, with the goal of minimizing data redundancy and improving data integrity.
13. **What is a primary key?**
    **Answer:** A specific column (or set of columns) in a database table that uniquely identifies every row in that table.
14. **What is a foreign key?**
    **Answer:** A column (or set of columns) in one table that references the primary key of another table, creating a link between the two tables to enforce referential integrity.
15. **What is indexing?**
    **Answer:** A database performance technique that creates a data structure (an index) on one or more columns to speed up the retrieval of rows, similar to an index at the back of a book.