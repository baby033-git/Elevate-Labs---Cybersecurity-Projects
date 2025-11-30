"""
Password Strength Analyzer + Custom Wordlist Generator
Project 1 - Cybersecurity Internship (Elevate Labs)

Features:
- Analyze password strength (length, uppercase, lowercase, digits, symbols)
- Calculate password entropy score
- Generate custom wordlists based on user details
- Apply leetspeak variations and year patterns
- Export wordlist to a .txt file
"""

import string

def analyze_password(pwd):
    score = 0
    remarks = []

    if len(pwd) >= 8:
        score += 1
        remarks.append("✔ Good length")
    else:
        remarks.append("✘ Weak length (< 8 chars)")

    if any(c.islower() for c in pwd):
        score += 1
        remarks.append("✔ Contains lowercase")
    else:
        remarks.append("✘ No lowercase letters")
    
    if any(c.isupper() for c in pwd):
        score += 1
        remarks.append("✔ Contains uppercase")
    else:
        remarks.append("✘ No uppercase letters")

    if any(c.isdigit() for c in pwd):
        score += 1
        remarks.append("✔ Contains digits")
    else:
        remarks.append("✘ No digits")

    if any(c in string.punctuation for c in pwd):
        score += 1
        remarks.append("✔ Contains symbols")
    else:
        remarks.append("✘ No special characters")

    entropy = len(set(pwd)) * len(pwd)

    strength = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]

    return strength[score], entropy, remarks


def generate_wordlist(name, pet, year):
    words = []

    base = [name, pet, name+pet, pet+name]

    for b in base:
        words.append(b)
        words.append(b + year)
        words.append(year + b)

    leet = {
        "a": "@",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "$"
    }

    for b in base:
        mutated = "".join(leet.get(c, c) for c in b.lower())
        words.append(mutated)
        words.append(mutated + year)

    return list(set(words))


def save_wordlist(words):
    file = "custom_wordlist.txt"
    with open(file, "w") as f:
        for w in words:
            f.write(w + "\n")
    print(f"[+] Wordlist saved as {file}")


def main():
    print("=== PASSWORD STRENGTH ANALYZER ===")
    pwd = input("Enter a password to analyze: ")

    strength, entropy, remarks = analyze_password(pwd)
    print("\nPassword Strength:", strength)
    print("Entropy Score:", entropy)
    print("\nDetails:")
    for r in remarks:
        print("-", r)

    print("\n=== CUSTOM WORDLIST GENERATOR ===")
    name = input("Enter your name: ")
    pet = input("Enter pet/fav word: ")
    year = input("Enter year (ex: 2004): ")

    words = generate_wordlist(name, pet, year)
    save_wordlist(words)

    print("\n[+] Wordlist generated with", len(words), "entries.")
    print("[+] Project Completed Successfully!")


if __name__ == "__main__":
    main()
