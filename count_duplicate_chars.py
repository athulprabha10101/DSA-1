def count_duplicate_chars(mystring):
    dup_chars = []
    for char in mystring:
        if mystring.count(char) >1 and char not in dup_chars:
            dup_chars.append(char)
    return dup_chars

d= "hellhoo"
print(count_duplicate_chars(d))