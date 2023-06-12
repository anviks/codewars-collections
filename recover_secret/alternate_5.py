def recover_secret(triplets):
    letters = {}
    for i in range(5):
        for a, b, c in triplets:
            letters[a] = letters.get(a, 0)
            letters[b] = letters.get(b, 0) + 1 + letters.get(a, 0)
            letters[c] = letters.get(c, 0) + 10 + letters.get(b, 0) * 10 + letters.get(a, 0)
    return ''.join([letter[0] for letter in sorted(letters.items(), key=lambda x: x[1])])
