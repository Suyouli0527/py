def main():
    word = "ijklmnop"
    s = ""
    length = len(word)
    for i in range(length // 2):
        if i < 2:
            c1 = word[3]
            c2 = word[6-3*i]
        else :
            c1 = word[6*(i-2)]
            c2 = word[7]
        s = s + c1 + c2
    print(s)
main()