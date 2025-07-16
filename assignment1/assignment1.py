# Write your code here.

#Task 1
def hello():
    return "Hello!"
#Task 2
def greet(name):
    return f"Hello, {name}!"
#Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
#Task 4
def data_type_conversion(value, type_name):
    try:
        if type_name == "int":
            return int(value)
        elif type_name == "float":
            return float(value)
        elif type_name == "str":
            return str(value)
        else:
            return f"Unknown type: {type_name}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type_name}."

#Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    except:
        return "Invalid data was provided."

#Task 6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

#Task 7
def student_scores(stat, **kwargs):
    if stat == "best":
        return max(kwargs, key=kwargs.get)
    elif stat == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid stat request."
#Task 8
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()
    title = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            title.append(word.capitalize())
        else:
            title.append(word.lower())

    return " ".join(title)
#Task 9
def hangman(secret, guess):
    result = ""
    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
    return result
#Task 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
        elif word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1
            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)