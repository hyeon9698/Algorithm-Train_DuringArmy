def main():
    x = input()
    count1 = 0
    count2 = 0
    for i in x:
        if i == '(':
            count1 += 1
        elif i == ')':
            count2 += 1
    if count1 == count2:
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    main()
