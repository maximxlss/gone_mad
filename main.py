from random import random


print("Input any number in decimal (including complex as a + bi)")


def int_or_float(s):
    try:
        return int(s)
    except ValueError as e:
        print(e)
        return float(s)


def random_case(s):
    return "".join(c.lower() if random() < 0.5 else c.upper() for c in s)


def add_random_underscores(s):
    new_s = ""
    can_add = True
    underscore_probability = 0.2

    for c in s:
        if can_add and random() < underscore_probability:
            new_s += "_"
            can_add = False
        else:
            can_add = True
        new_s += c

    return new_s


def process_one(x):
    is_negative = x < 0
    if is_negative:
        x *= -1

    m = int(x)
    x -= m
    e = 0
    while x > 0:
        x *= 2
        p = int(x)
        x -= p
        m = 2 * m + p
        e -= 1

    s = ""

    # sign for clarity obviously
    s += "-" if is_negative else "+"

    # hex string cuz it's the best number system for programming obviously
    # with underscores for readability obviously
    s += "0x" + add_random_underscores(hex(m)[2:])

    # dot for clarity obviously
    s += "."

    # exponent instead of point cuz it's clearer for math obviously
    s += "p"
    if e <= 0:
        s += "-"
        e *= -1
    p = str(e)
    s += p[0] + add_random_underscores(p[1:])

    # random case for some variety obviously
    s = random_case(s)

    return s


while True:
    s = input("> ").strip().replace(" ", "")

    i = s.find("-", 1)
    j = s.find("+", 1)

    if any(c not in ".+-0123456789i" for c in s) or (i != -1 and j != -1):
        print("Only decimal complex numbers are supported, no exponents or hex.")
        continue

    i = max(i, j)

    if i == -1:
        x = int_or_float(s)
        s = process_one(x)
        print(s)
    elif s.endswith("i"):
        a, b = s[:i], s[i:-1]
        x, y = int_or_float(a), int_or_float(b)
        s1, s2 = process_one(x), process_one(y)
        print(f"{s1}{s2}i")
    else:
        print("what?")
