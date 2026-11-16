# Encryption and Secure Password Storage

> **Course:** Information Assurance and Security  
> **Module:** 18 — Encryption  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Hello students! Today, we are covering the topic of **Encryption**. We have discussed this before, but today we will put it into practice. We will be using **PHP** and **MySQL** to code a simple registration and login system. This lab will show you exactly how encryption works and what it looks like from the database side.

**Quick Review:**
Can you still recall the purpose of encryption? 
*   *Hint:* Encryption is a security mechanism that scrambles data so it becomes unreadable to anyone who doesn't have the decryption key.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Understand the importance of encryption.
2.  Code simple encrypted passwords.

![Encryption Concept](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Why is Encryption Important?
Encryption scrambles your password so it is unreadable by hackers or even database administrators. Encryption protects your password while it is sitting in a server (data at rest) and offers more protection as your password passes across the internet (data in transit).

**The Danger of Plaintext Passwords**
Imagine you create a very strong password, such as one with uppercase and lowercase letters, symbols, and numbers. 
*   *Example:* `31?Ax#Ks8vH@h9R!2`
You use this password across your devices because you know it cannot be brute-forced.

However, if the developer of the system *did not encrypt the password*, the database administrator will simply see this in the MySQL database:
`| id | first_name | last_name | username | password |`
`| 7 | Harry | Potter | PinkHarryPotter | 31?Ax#Ks8vH@h9R!2 |`

Now, all your accounts are compromised. What if the administrator's account is hacked? The attacker sees the unencrypted password, and you are in real trouble.

> **Important Note:** This is why we need encryption. We need to protect our passwords and any important data we transfer so that no one can access your account.

### Understanding Hashing (Technically)
While the module refers to this as "encryption," the PHP function `password_hash()` actually performs **Hashing**. Hashing is a one-way cryptographic function, meaning it cannot be reversed (decrypted). Instead, during login, the system hashes the entered password and compares it to the stored hash.

**Highest Level of Encryption**
As of today, the highest level of encryption for public use is **AES 256**. It has a high level of complexity and is considered virtually impenetrable. If you can incorporate AES 256 into your projects, that is fantastic.

### Brute Force Hacking
It is important to note that encryption alone is not enough. If your password is very simple (e.g., "password123"), it can easily be brute-forced or found in a dictionary. Modern encryption is so powerful that the responsibility now falls on the user to create strong passwords.

Brute force hacking is easily countered by proper passwords. The table below shows how long it would take a hacker to brute force your password in 2023.

| Number of Characters | Numbers Only | Lowercase Letters | Upper and Lowercase Letters | Numbers, Upper and Lowercase Letters | Numbers, Upper and Lowercase Letters, Symbols |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4** | Instantly | Instantly | Instantly | Instantly | Instantly |
| **5** | Instantly | Instantly | Instantly | Instantly | Instantly |
| **6** | Instantly | Instantly | Instantly | Instantly | Instantly |
| **7** | Instantly | Instantly | 1 sec | 2 secs | 4 secs |
| **8** | Instantly | Instantly | 28 secs | 2 mins | 5 mins |
| **9** | Instantly | 3 secs | 24 mins | 2 hours | 6 hours |
| **10** | Instantly | 1 min | 21 hours | 5 days | 2 weeks |
| **11** | Instantly | 32 mins | 1 month | 10 months | 3 years |
| **12** | 1 sec | 14 hours | 6 years | 53 years | 226 years |
| **13** | 5 secs | 2 weeks | 332 years | 3k years | 15k years |
| **14** | 52 secs | 1 year | 17k years | 202k years | 1m years |
| **15** | 9 mins | 27 years | 898k years | 12m years | 77m years |
| **16** | 1 hour | 713 years | 46m years | 779m years | 5bn years |
| **17** | 14 hours | 18k years | 2bn years | 48bn years | 380bn years |
| **18** | 6 days | 481k years | 126bn years | 2tn years | 26tn years |

---

## C. Analogies and Use Cases

### The "Coat Check" Analogy
Think of a database as a coat check at a club.
*   **Plaintext:** You hand over your coat, and the attendant just hangs it on a rack with your name tag. Anyone who walks by can steal your coat or go through your pockets.
*   **Encryption/Hashing:** The attendant puts your coat in a locked, opaque box. They give you a ticket (the hash). They don't know what's inside the box, and neither does anyone else. When you want your coat back, you give them the ticket. They verify the ticket matches the box and give you your coat. If someone steals the ticket, the attendant verifies the ticket matches the box. 
*   **Salting (The Magic of Bcrypt):** If two people have the same coat, the attendant still uses different boxes and different tickets. This prevents a thief from realizing two people have the same coat.

### Real-World Use Case: The LinkedIn Breach (2012)
In 2012, LinkedIn suffered a massive data breach. Over 6 million passwords were stolen. The passwords were stored using SHA-1 hashing without salting (a weakness). Hackers were able to easily crack millions of these passwords using rainbow tables and brute force because the hashes were predictable. This event highlighted the necessity of using strong, salted hashing algorithms like **Bcrypt** (which we are using in this lab).

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   Never store passwords in plaintext. Always use strong hashing algorithms like **Bcrypt** or encryption like **AES 256**.
*   PHP provides built-in functions (`password_hash()` and `password_verify()`) to handle password security securely.
*   Brute-force attacks are defeated by a combination of strong encryption and complex, long passwords (12+ characters with symbols).
*   Hashing is a one-way process; you cannot "decrypt" a hash. You can only verify if an input matches the hash.

### Frequently Asked Questions
**1. Other uses of Encryption?**
**A:** As mentioned, encryption can be used in transferring files or moving data. This way, any Man-in-the-Middle (MitM) attacks can be easily prevented because the intercepted data is unreadable.

**2. What is the difference between Hashing and Encryption?**
**A:** Encryption is a two-way process (you can encrypt and decrypt with a key). Hashing is a one-way process (you cannot reverse a hash). Password storage should always use *hashing* (like bcrypt), not reversible encryption.

**3. Why did we use `password_hash` instead of MD5 or SHA1?**
**A:** MD5 and SHA1 are outdated and vulnerable to collision and brute-force attacks. `password_hash` uses Bcrypt, which automatically includes a random "salt" for every password, making it highly resistant to rainbow table attacks.

---

## E. Guided Drills / Code Projects

### Lab Activity: Implementing Password Encryption
**Project Overview:** 
In this lab, we will modify a simple login and register system to use encryption.

**Prerequisites:**
*   XAMPP running (Apache & MySQL)
*   A code editor (Notepad++ or similar)
*   The provided `encryptionias2` folder and database file

**Step-by-Step Instructions:**

**Step 1: Initial Setup (Trial 1)**
1.  Import the database to your localhost MySQL.
2.  Copy the `encryptionias2` folder to your `htdocs` directory.
3.  Register a new user (e.g., `user1`, password `password1`).
4.  Check the database. Notice that the password is stored as **plaintext** (`password1`). This is a critical vulnerability.

**Step 2: Implementing Encryption (Trial 2)**
1.  Open `register.php`.
2.  Locate line 22 (or the line before the SQL INSERT query).
3.  Add the following code to hash the password:
    ```php
    $encryptpass = password_hash($pass, PASSWORD_BCRYPT);
    ```
4.  Modify your SQL INSERT query to use `$encryptpass` instead of `$pass`:
    ```php
    $sql = "INSERT INTO users (`id`, `first_name`, `last_name`, `username`, `password`) VALUES (0, '$fname', '$lname', '$uname', '$encryptpass')";
    ```
5.  Register a new user (e.g., `user2`, password `password2`).
6.  Check the database. You should now see a long, scrambled string starting with `$2y$10$...`. This is the Bcrypt hash.

**Step 3: Verifying Passwords (Login)**
1.  Because passwords are hashed, you cannot simply compare `$pass == $password` in `login.php`.
2.  Open `login.php` and find lines 29 and 32.
3.  Replace the password fetching and comparison logic with:
    ```php
    // Line 29
    $hashed_pass = $row["password"];

    // Line 32
    if (password_verify($pass, $hashed_pass)) {
        // Login successful
    }
    ```
4.  Test your login with `user2` and `password2`. It should work successfully.

### Solo Project Update: Applying Encryption
Apply encryption on your project's system passwords. If you are using PHP, `bcrypt` should be sufficient.
*   **Task:** Ensure that your registration system hashes passwords before inserting them into the database.
*   **Task:** Ensure that your login system uses `password_verify()` to check credentials.

---

## F. Skill-Building Check

### Check for Understanding (10 mins Quiz)

**Exercise 1:**
Try to register another user, name it `user3`, and input the **same password** as previously (`password2`). Compare the 2 passwords in the database MySQL Localhost. What did you observe?

*Guidance:* You will observe that the two hashes are **completely different**, even though the passwords are identical. This is because Bcrypt automatically generates a unique random **salt** for each password before hashing. This prevents attackers from knowing that two users have the same password and defeats pre-computed rainbow table attacks.

**Multiple Choice:**

**1. Which PHP function is used to securely hash a password during registration?**
A. `md5()`
B. `sha1()`
C. `password_hash()`
D. `encrypt()`
**Correct Answer: C** (The `password_hash()` function is the modern, secure standard for PHP).

**2. What is the primary danger of storing passwords in plaintext?**
A. The database runs slower.
B. Anyone with database access can read the passwords directly.
C. The website will not load.
D. Users will forget their passwords.
**Correct Answer: B** (Plaintext storage exposes passwords immediately upon a data breach).

**3. Which of the following is considered the highest level of encryption for public use?**
A. MD5
B. SHA-1
C. AES 256
D. Bcrypt
**Correct Answer: C** (AES 256 is a robust symmetric encryption standard).

**4. True or False: You can decrypt a Bcrypt hash to retrieve the original plaintext password.**
**Correct Answer: False** (Bcrypt is a one-way hashing function, not a reversible encryption algorithm).