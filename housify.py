from math import sqrt

def housify(text):
    text = text.upper().replace(" ", "")
    nearest_square = round(sqrt(len(text))) ** 2
    letters_perline = int(sqrt(nearest_square))
    t_len = len(text)
    index = 0
    for i in range(t_len // letters_perline):
        print(text[index:index+letters_perline])
        index += letters_perline
        t_len -= letters_perline

    print(text[index:], end = "")
    if t_len > 0:
        print("." * (letters_perline - t_len))


def main():
    housify(input("Enter text to housify: "))


if __name__ == "__main__":
    main()
