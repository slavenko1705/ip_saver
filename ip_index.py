a = ["1", "2", "9", "10"]
b = "9"

for i, el in enumerate(a):
    print(f"el: {el}, index: {i}")
    
    if b in a:
        print("ip_адреса дублюється")
        break
    elif int(b) > int(el) and i == (len(a) - 1):
        a.append(b)
        break
    elif int(b) > int(el):
        continue
    else:
        a = a[:i] + list(b) + a[i:]
        break
