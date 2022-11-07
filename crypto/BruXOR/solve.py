chiper = "q{vpln'bH_varHuebcrqxetrHOXEj"

for i in range(0xff):
    result = ''
    for j in chiper:
        result += chr(ord(j) ^ i)
    print(f"KEY {i}: {result}")

# the true flag will be find at the key 23
