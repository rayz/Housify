import pyperclip
from math import sqrt

def housify(text):
    res = []
    text = text.upper().replace(" ", "")
    nearest_square = round(sqrt(len(text))) ** 2
    letters_perline = int(sqrt(nearest_square))
    t_len = len(text)
    index = 0

    for i in range(t_len // letters_perline):
        res.append(text[index:index+letters_perline])
        index += letters_perline
        t_len -= letters_perline
    last_line = text[index:]

    if t_len > 0:
        last_line += "." * (letters_perline - t_len)

    res.append(last_line)
    pyperclip.copy("\n".join(res))

    print("\n".join(res), end = "")
    print("House successfully copied to clipboard!")

def main():
    housify(input("Enter text to housify: "))

if __name__ == "__main__":
    main()
