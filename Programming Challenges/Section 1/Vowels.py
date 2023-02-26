sentence = input("Please enter a sentence of your choice.")
sentence = sentence.lower()
a = sentence.count("a");
e = sentence.count("e");
i = sentence.count("i");
o = sentence.count("o");
u = sentence.count("u");
print("Your sentence contained the following:")
print("a =", a)
print("e =", e)
print("i =", i)
print("o =", o)
print("u =", u)
print("This is a total of", a + e + i + o + u, "vowels.")