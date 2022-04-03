def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Herry is a good      "
n = remove_and_split(this, "a")
print(n)
# print(this)
# print(this.strip())
