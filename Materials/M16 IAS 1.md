# Cryptography, Passwords, and Authenticators

> **Course:** Information Assurance and Security  
> **Module:** 16 — Cryptography, Passwords and Authenticators  
> **Learning Format:** Individual Activity (Solo Work)

---

## A. Lesson Preview & Review

Welcome back, future security officers! Today, we are stepping into the practical world of Security and IT. We are going to get our hands a bit dirty with **Cryptography**. Don't worry, all you need is a browser and an internet connection.

When you hear the word "cryptography," what comes to mind? If you thought of "passwords," you are not far off! Today, we will explore the core concepts of cryptography, including **Encryption**, **Decryption**, and **Hashing**. We will also look at how these concepts apply to creating and storing secure passwords.

**Learning Targets:**
By the end of this module, you will be able to:
1.  Discuss the importance of cryptography and the characters you use in passwords.
2.  Apply basic encryption and decryption in codes and through the internet.

![Cryptography Concept](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80)

---

## B. Main Lesson

### Core Concepts of Cryptography

**Cryptography** is the science of secure communication techniques. It allows only the authorized and authenticated sender and intended receiver of a message to view its contents. In other words, it is the practice of masking information so that it is only understandable by the sender and the receiver.

**Encryption** is the process of converting an original message (plaintext) into a form that is unreadable to unauthorized individuals (ciphertext). It ensures that anyone without the tools to convert the encrypted message back cannot read it.

**Decryption** is the reverse process. It converts the ciphertext message back into plaintext so that it can be readily understood.

### Understanding Hashing
While we are on the topic of cryptography, we must also discuss **Hashing**. A hash function is a process of changing an input into a **hash sum**. 

*   **Fixed Output Size:** Regardless of the number of inputted characters, the resulting hash sum always has the same size.
*   **One-Way Nature:** A person cannot mathematically translate a hash back into the original input. However, a computer can verify if a guessed input matches a hash.
*   **Deterministic:** The same input will always produce the exact same hash.

**Example of Hashing:**
| Input | Hash Function | Hash Sum (Truncated for readability) |
| :--- | :--- | :--- |
| Fox | Hash function | `DFCD3454 BBEA788A...` |
| The red fox runs across the ice | Hash function | `52ED879E 70F71D92...` |
| The red fox walks across the ice | Hash function | `46042841 935C7FB0...` |

### Cryptographic Hash Functions & Technologies
**Cryptographic Hash Function** is applying cryptography in hashing. This means it is technically impossible to decrypt an encrypted message unless you know exactly what hashing technology was used. 

Here are a few common cryptographic technologies used today:

| Technology | Full Name | Output Size | Status / Notes |
| :--- | :--- | :--- | :--- |
| **MD5** | Message Digest 5 | 128-bit hash value | Considered outdated; vulnerable to collision attacks. |
| **SHA-1** | Secure Hash Algorithm 1 | 160-bit (20-byte) hash value (represented as a 40-digit hexadecimal) | Considered flawed and easily hacked, but still occasionally used. |
| **AES / RSA** | Advanced Encryption Standard / Rivest-Shamir-Adleman | Varies | Modern, advanced cryptographic technologies. |

**Code Examples:**
Here is how you can apply MD5 hashing in different programming languages.

```php
<?php
// PHP Example
$str = "Hello World";
echo md5($str);
?>
```

```csharp
// C# Example
public static string CreateMD5(string input)
{
    // Use input string to calculate MD5 hash
    using (System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create())
    {
        byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(input);
        byte[] hashBytes = md5.ComputeHash(inputBytes);
        return Convert.ToHexString(hashBytes); // .NET 5+
    }
}
```

### The Reality of Cryptography and Password Strength
There is a "sad reality" to cryptography: Hashing actually slows down the process of transmitted information because the data must be encrypted and decrypted. However, with modern technology, this slowdown is negligible.

The bigger issue is the **endless race**. As technology improves, hackers are equally equipped to exploit weaknesses in outdated algorithms like MD5 and SHA-1. 

**Password Strength**
This is why creating a password requires specific parameters: **Uppercase, Lowercase, Number, Symbol, and 8+ characters**. This complexity ensures that the password can be encrypted but is very difficult to decrypt without knowing the exact decryption process. 

> **Pro Tip:** When using online MD5 decryption tools, you may find that some passwords "cannot be decrypted." This is because these tools rely on databases of previously cracked hashes. If the exact text isn't in their database, they cannot reverse the hash. This highlights why complex, unique passwords are significantly harder for hackers to crack using pre-computed tables (rainbow tables).

---

## C. Analogies and Use Cases

### The "Lockbox" Analogy
Think of **Encryption** as putting a letter inside a strong, locked box. Anyone can carry the box (transmit the data), but only the person with the correct key can open it and read the letter (**Decryption**).

Think of **Hashing** as taking a fingerprint of that letter. You can't rebuild the letter from the fingerprint, but if you suspect a specific letter matches, you can compare fingerprints to verify it's the exact same document. 

### Real-World Use Case: Password Storage
When you create an account on a website, the company should never store your password in plain text. Instead, they run your password through a hashing algorithm (like SHA-256) and store the hash. When you log in, they hash the password you just typed and compare it to the stored hash. If they match, you are authenticated. This way, even if the database is breached, the hackers only get hashes, not the actual passwords.

---

## D. Lesson Wrap-Up / FAQs

### Key Takeaways
*   **Cryptography** secures communication by masking information.
*   **Encryption** converts plaintext to ciphertext; **Decryption** converts it back.
*   **Hashing** is a one-way function that produces a fixed-size output (hash sum).
*   MD5 and SHA-1 are common but outdated algorithms. AES and RSA are more secure modern alternatives.
*   Strong passwords (Uppercase, Lowercase, Number, Symbol, 8+ characters) are difficult to crack because they resist brute-force and dictionary attacks.

### Frequently Asked Questions
**1. If MD5 and SHA-1 are flawed, why are they still used?**
**A:** They are fast and computationally inexpensive. Many legacy systems still rely on them. However, for new systems, stronger algorithms like SHA-256 or bcrypt are highly recommended.

**2. Can a hash be reversed?**
**A:** No. Hashing is a one-way mathematical function. You cannot "decrypt" a hash. You can only guess the input and hash your guess to see if it matches.

**3. What is the difference between Encryption and Hashing?**
**A:** Encryption is a two-way process (you can decrypt it with a key). Hashing is a one-way process (you cannot reverse it). Encryption is used for transmitting data securely; hashing is used for verifying data integrity and storing passwords.

**4. Why does my password require a symbol and a number?**
**A:** Adding symbols and numbers dramatically increases the "search space" a hacker must explore to guess your password. It protects against dictionary attacks (guessing common words) and brute-force attacks (trying every possible combination).

---

## E. Guided Drills / Code Projects

### Solo Project: Encryption and Decryption Exercise
**Project Overview:** 
For this module, you will complete a practical lab exercise to see cryptography in action. You will use online tools to encrypt and decrypt strings.

> **Important Note:** This was originally designed as a group activity, but we are adapting it as a **solo activity**. You will complete the exercises individually to better understand how hashing works.

**Project Guidelines:**
*   **Format:** Individual work.
*   **Objective:** Use an online MD5/SHA-1 hash generator and an MD5 decryption tool to complete the exercises below.
*   **Submission:** Document your findings in your project folder.

**Step-by-Step Deliverable:**

**Part 1: Encryption Exercise**
Use a standard online hash generator (like `md5hashgenerator.com`). Encrypt the following sentences and record their MD5 and SHA-1 hashes:

1.  **The right man in the wrong place can make all the difference in the world**
    *   MD5: ________________________________________________
    *   SHA1: _______________________________________________
2.  **Praise the sun**
    *   MD5: ________________________________________________
    *   SHA1: _______________________________________________
3.  **Do a barrel roll**
    *   MD5: ________________________________________________
    *   SHA1: _______________________________________________
4.  **I am the swarm**
    *   MD5: ________________________________________________
    *   SHA1: _______________________________________________
5.  **The cake is a lie**
    *   MD5: ________________________________________________
    *   SHA1: _______________________________________________

**Part 2: Decryption Exercise**
Use an online MD5 decryption tool (like `md5online.org/md5-decrypt.html`). Decrypt the following MD5 hashes:

1.  `1036ba3c4ed2c021e8f5e2641c8a23e3`
    *   Text: ________________________________________________
2.  `45ea37a8b034ece4d08639d18d913ad0`
    *   Text: ________________________________________________
3.  `bb3ccd5881d651448ded1dac904054ac`
    *   Text: ________________________________________________
4.  `e150616b3c0801e894e0cc6274f84a3e`
    *   Text: ________________________________________________
5.  `e0d9d3862dfb270de65719d43749df5e`
    *   Text: ________________________________________________

**Part 3: The "Cannot Be Decrypted" Scenario**
1.  Encrypt the following string using the hash generator: `PaSsWord123?!`
    *   MD5: ________________________________________________
2.  Now, take that MD5 hash and try to decrypt it using the MD5 decryption tool.
    *   **What happened?** (Write your observation below)
    *   **Why is this the case?** (Write your explanation below)

---

## F. Skill-Building Check

### Part 1: Short Essay

**1. When do we apply Hashing and Cryptography? And why do we need to apply it?**
*Guidance:* Your answer should discuss that we apply cryptography when transmitting sensitive data over insecure networks (like the internet) to ensure confidentiality. We apply hashing when storing passwords or verifying file integrity, because it allows us to verify data without storing the original plaintext.

**2. What is the sad part of the improvement of our technologies?**
*Guidance:* The "sad part" is the endless race between security professionals and hackers. As technology improves to make encryption stronger, hackers also gain access to better processing power and tools to crack those encryptions. Additionally, even though modern technology makes encryption fast, there is always an inherent overhead (slowing down) to securing data.

### Part 2: Multiple Choice

**3. What is the process of converting an original message into a form that is unreadable to unauthorized individuals?**
A. Decryption
B. Hashing
C. Encryption
D. Authentication
**Correct Answer: C** (Encryption turns plaintext into ciphertext).

**4. Which cryptographic technology produces a 128-bit hash value?**
A. SHA-1
B. MD5
C. AES
D. RSA
**Correct Answer: B** (MD5 produces a 128-bit hash).

**5. What is a key characteristic of a hash sum?**
A. It can be easily decrypted to reveal the original input.
B. Its size changes depending on the length of the input.
C. Its size remains the same regardless of the input length.
D. It only works for numbers, not text.
**Correct Answer: C** (Hashing produces a fixed-size output regardless of input size).

**6. Why is a password like `PaSsWord123?!` difficult to decrypt using an online MD5 decryption tool?**
A. Because MD5 is a two-way encryption algorithm.
B. Because the tool uses a database of known hashes, and this specific complex string hasn't been cracked and stored yet.
C. Because symbols are not allowed in MD5 hashing.
D. Because the internet cannot process complex hashes.
**Correct Answer: B** (Online decryption tools rely on pre-computed databases of known passwords. Unique or complex passwords often aren't in these databases).