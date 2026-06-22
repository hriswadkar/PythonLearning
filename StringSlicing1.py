# String Slicing Examples
text = "Python"

print(text[0])      # Output: 'P'
print(text[1])      # Output: 'y'
print(text[-1])     # Output: 'n'
print(text[0:3])    # Output: 'Pyt'
print(text[3:])     # Output: 'hon'
print(text[:3])     # Output: 'Pyt'
print(text[::2])    # Output: 'Pto'
print(text[::-1])   # Output: 'nohtyP'
print(text[1:5:2])  # Output: 'yh'
print(text[5:1:-1]) # Output: 'noh'
print(text[10:])    # Output: '' (empty string, out of range)
print(text[-10:])   # Output: 'Python' (entire string, out of range)
print(text[:])      #Output: 'Python' (entire string)

text = "Hello"
print(text.upper())  # Output: 'HELLO'
print(text.lower())  # Output: 'hello'
print(text.capitalize())  # Output: 'Hello'
print(text.title())  # Output: 'Hello'
print(text.strip())  # Output: 'Hello' (removes leading/trailing whitespace)
print(text.replace("l", "L"))  # Output: 'HeLLo'
print(text.split("e"))  # Output: ['H', 'llo']
print(text.join(["A", "B", "C"]))  # Output: 'AHellolBHelloC'
print("x" in text)  # Output: False
print(text.startswith("He"))  # Output: True
print(text.endswith("lo"))  # Output: True