import hashlib
import string
from itertools import product
from multiprocessing import Pool, cpu_count


hash1 = "2a07038481b64a934495e5a91d011ecbf278aba8c5263841e1d13f73975d5397"
hash2 = "cd6e58d947e2f7ace23cb6d602daa1ae46934c3c1f4800bfd25e6af2b555f6f5"
hash3 = "84b9e0298b1beb5236b7fcd2dd67e67abf62d16fe6d591024178790238cb4453"
rockyou_path = "rockyou.txt"
vowels = "aeiouyAEIOUY"

qwerty_right = {
    '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8',
    '8': '9', '9': '0', '0': '1',
    'q': 'w', 'w': 'e', 'e': 'r', 'r': 't', 't': 'y', 'y': 'u', 'u': 'i',
    'i': 'o', 'o': 'p', 'p': 'q',
    'a': 's', 's': 'd', 'd': 'f', 'f': 'g', 'g': 'h', 'h': 'j', 'j': 'k',
    'k': 'l', 'l': 'a',
    'z': 'x', 'x': 'c', 'c': 'v', 'v': 'b', 'b': 'n', 'n': 'm', 'm': 'z'
}

def crack_password1():
    print("[*] Cracking Password 1...")
    with open(rockyou_path, "r", encoding="utf-8", errors="ignore") as f:
        for word in f:
            word = word.strip()
            for upper in string.ascii_uppercase:
                prepended = upper + word
                if len(prepended) < 2:
                    continue
                swapped = prepended[1] + prepended[0] + prepended[2:]
                rotated = swapped[-3:] + swapped[:-3]
                for year in range(1900, 2026):
                    candidate = rotated + str(year)
                    if hashlib.sha256(candidate.encode()).hexdigest() == hash1:
                        print(f"[+] Password 1 Cracked: {candidate}")
                        return candidate
    return None

def caesar_shift(text, shift):
    shifted = ""
    for char in text:
        if char.isalpha():
            shifted += chr(((ord(char) - 97 + shift) % 26) + 97)
        else:
            shifted += char
    return shifted

def qwerty_map(text):
    return ''.join(qwerty_right.get(c, c) for c in text)

def try_password2(word):
    word = word.lower()
    for shift in range(1, 26):
        shifted = caesar_shift(word, shift)
        qwerty = qwerty_map(shifted)
        reversed_final = qwerty[::-1]
        if hashlib.sha256(reversed_final.encode()).hexdigest() == hash2:
            return reversed_final
    return None

def toggle_consonants(text):
    return ''.join(c.swapcase() if c.lower() not in vowels and c.isalpha() else c for c in text)

def vowel_positions(text):
    return [i for i, c in enumerate(text) if c in vowels]

def toggle_vowel_cases(text):
    positions = vowel_positions(text)
    for combo in product([0, 1], repeat=len(positions)):
        text_list = list(text)
        for i, pos in enumerate(positions):
            if combo[i] == 1:
                text_list[pos] = text_list[pos].swapcase()
        yield ''.join(text_list)

def interleave(a, b):
    return ''.join(x + y for x, y in zip(a, b))

def try_password3(word):
    word = word.strip()
    if len(word) % 2 != 0 or len(word) > 14:
        return None
    mid = len(word) // 2
    h1, h2 = word[:mid], word[mid:]
    h1_toggled = toggle_consonants(h1)
    for h2_variant in toggle_vowel_cases(h2):
        combined = interleave(h1_toggled, h2_variant)
        if hashlib.sha256(combined.encode()).hexdigest() == hash3:
            return combined
    return None

#main
def crack_all():
    #crack
    p1 = crack_password1()

    #load
    with open(rockyou_path, "r", encoding="utf-8", errors="ignore") as f:
        words = [line.strip() for line in f if line.strip()]

    #crack_p2
    print("[*] Cracking Password 2 with multiprocessing...")
    with Pool(cpu_count()) as pool:
        for result in pool.imap_unordered(try_password2, words):
            if result:
                print(f"[+] Password 2 Cracked: {result}")
                p2 = result
                break
        else:
            p2 = None

    #crack_p3
    print("[*] Cracking Password 3 with multiprocessing...")
    with Pool(cpu_count()) as pool:
        for result in pool.imap_unordered(try_password3, words):
            if result:
                print(f"[+] Password 3 Cracked: {result}")
                p3 = result
                break
        else:
            p3 = None

    #flag_output
    if p1 and p2 and p3:
        print(f"\n🏁 FLAG: L3AK{{{p1}_{p2}_{p3}}}")
    else:
        print("\n[-] One or more passwords could not be cracked.")

if __name__ == "__main__":
    crack_all()

