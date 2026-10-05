a = ["1", "2", "9", "10"]
b = "0"

for i, el in enumerate(a):
    print(f"el: {el}, index: {i}")
    
    if int(b) > int(el) and i == (len(a) - 1):
        a.append(b)
        # c = a
        print("1")
        break
    elif int(b) > int(el):
        print("2")
        continue
    else:
        a = a[:i] + list(b) + a[i:]
        print("3")
        break

# print(needed_ip_index)


print(a)