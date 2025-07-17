
If you thought rules were easy after the last challenge, think again! I've concocted more devious password mangling rules to push the limits of your cracking knowledge (and possibly your CPU...):

- **Password 1:** Prepend 1 uppercase letter, Swap the first 2 characters, Rotate it to the right 3 times, Append a 4-digit year since 1900.
- **Password 2:** Lowercase the entire password. Apply a random caesar cipher shift to all the letters in the password. Then, replace each alphanumeric character with its right neighbor on the QWERTY keyboard. Finally, reverse it.
- **Password 3:** Split the password in half, toggle the case of every consonant in the first half, randomly toggle the case of all vowels in the second half, then interleave the halves together. Assume password has an even length and is no more than 14 characters. The letter Y is considered a vowel for the purposes of this challenge.

`2a07038481b64a934495e5a91d011ecbf278aba8c5263841e1d13f73975d5397` `cd6e58d947e2f7ace23cb6d602daa1ae46934c3c1f4800bfd25e6af2b555f6f5` `84b9e0298b1beb5236b7fcd2dd67e67abf62d16fe6d591024178790238cb4453`

Use the rockyou.txt wordlist.

Flag format: `L3AK{pass1_pass2_pass3}`

Author: `Suvoni`



### Overview

In this challenge, we were given three SHA256 hashes corresponding to passwords that were transformed according to specific mangling rules. Our goal was to reverse these transformations (i.e., brute-force) using the RockYou wordlist and custom logic for each rule, then assemble the final flag in the format `L3AK{pass1_pass2_pass3}`.

### Tools and Environment

- **Python 3**: Used for scripting and hashing via the `hashlib` module.
    
- **rockyou.txt** wordlist: A comprehensive list of common passwords for brute-forcing.
    
- **multiprocessing** module: To parallelize heavy computations across CPU cores.
    

#### Dependencies

No external Python packages are required; the script relies solely on Python’s standard library. Ensure you have:

```
sudo apt install python3 python3-pip
gunzip /usr/share/wordlists/rockyou.txt.gz
cp /usr/share/wordlists/rockyou.txt .
```

### Password 1: Prepend Letter, Swap, Rotate, Append Year

**Transformation Steps**:

1. Prepend one uppercase letter (`A–Z`).
    
2. Swap the first two characters.
    
3. Rotate the string to the right by 3 positions.
    
4. Append a 4-digit year between 1900 and 2025.
    

**Reverse Strategy**:

- Iterate each word from `rockyou.txt`.
    
- For every uppercase letter, construct the candidate and perform the swap and rotation.
    
- Loop through all years (1900–2025), append each, compute SHA256, and compare to the target hash.
    

**Key Code Snippet**:

```
def crack_password1():
    for word in wordlist:
        for upper in string.ascii_uppercase:
            s = upper + word           # Prepend
            s = s[1] + s[0] + s[2:]     # Swap first two
            s = s[-3:] + s[:-3]         # Rotate right 3
            for year in range(1900, 2026):
                cand = s + str(year)
                if sha256(cand) == hash1:
                    return cand
```

### Password 2: Lowercase → Caesar Shift → QWERTY Neighbor → Reverse

**Transformation Steps**:

1. Lowercase the password.
    
2. Apply a Caesar cipher shift (`1–25`).
    
3. Map every character to its right neighbor on a QWERTY keyboard.
    
4. Reverse the entire string.
    

**Reverse Strategy**:

- Lowercase each candidate word.
    
- Try all 25 non-zero shifts.
    
- For each shifted string, translate each character using a predefined QWERTY mapping.
    
- Reverse the result, then hash and compare.
    

**Parallelization**: Because each candidate is independent, we used `multiprocessing.Pool` to distribute the workload across all CPU cores, returning early upon finding a match.

**Key Code Snippet**:

```
def try_password2(word):
    word = word.lower()
    for shift in range(1, 26):
        s = caesar_shift(word, shift)
        s = qwerty_map(s)
        s = s[::-1]
        if sha256(s) == hash2:
            return s
```

### Password 3: Split, Toggle Consonants/Vowels, Interleave

**Transformation Steps**:

1. Ensure the password length is even (≤14).
    
2. Split into two halves.
    
3. Toggle the case of every consonant in the first half.
    
4. For the second half, generate all combinations of vowel-case toggles (including `Y`).
    
5. Interleave the two halves character-by-character.
    

**Reverse Strategy**:

- Filter for even-length words.
    
- For each, apply consonant-case toggling to the first half.
    
- Use `itertools.product` to enumerate `2^n` vowel-case permutations in the second half.
    
- Interleave halves, hash, and compare.
    

**Key Code Snippet**:

```
def try_password3(word):
    mid = len(word)//2
    h1, h2 = word[:mid], word[mid:]
    h1 = toggle_consonants(h1)
    for h2_var in toggle_vowel_cases(h2):
        cand = interleave(h1, h2_var)
        if sha256(cand) == hash3:
            return cand
```

### Multiprocessing and Performance

- We used `cpu_count()` to spawn one worker per core.
    
- Both Password 2 & 3 tasks were submitted to worker pools with `imap_unordered`, enabling early exit on success.
    
- This approach drastically reduces wall-time compared to single-threaded brute-forcing.

![[Pasted image 20250713143147.png]]