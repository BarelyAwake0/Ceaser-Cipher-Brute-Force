import string

cipher = list(string.ascii_lowercase)
common_words = "common_words.csv"

with open(common_words, 'r') as file:
    common_words = file.read().splitlines()
    

def hack(string, key):
    count = 0

    #msg to list
    msg_low = string.lower()
    split_msg = msg_low.split(" ")

    chrs = []

    for word in split_msg:
        split_chrs = list(word)
        chrs.append(split_chrs)

    ciphers = []

    x = cipher.pop(0)
    cipher.append(x)

    hacked_attempt = []

    for word in chrs:
        for letter in word:
            for i in range(len(cipher)):
                if letter == cipher[i]:
                    decoded_pos = i - key
            decoded_chr = cipher[decoded_pos]
            hacked_attempt.append(decoded_chr)
        hacked_attempt.append(" ")
    hacked_word  = "".join(hacked_attempt)

    # word analysis
    split_hack = []
    split_hack = hacked_word.split(" ")

    score = 0

    for i in range(len(split_hack)):
        for j in range(len(common_words)):
            if split_hack[i] == common_words[j]:
                score += 1

    return [key, split_hack, score]


def bubbleSort(list):
    n = len(list)

    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if list[j][2] > list[j+1][2]:
                swapped = True
                list[j], list[j+1] = list[j+1], list[j]

        if not swapped:
            return list


msg = input("Enter your encrypted message...\n")

saved = []

for key in range(26):
    saved.append(hack(msg, key))
    # print(f"KEY #{key}: {hack(msg, key)}")

order_saved = bubbleSort(saved)

prob_data = order_saved[-1]
prob_key = prob_data[0]
prob_msg = " ".join(prob_data[1])

print(f"KEY #{prob_key}: {prob_msg}")
