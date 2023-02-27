def isRotation(a: str, b: str) -> bool:
    n = len(a)
    m = len(b)
    if (n != m):
        return False
  
    lps = [0 for _ in range(n)]
  
    length = 0
    i = 1
  
    lps[0] = 0
  
    while (i < n):
        if (a[i] == b[length]):
            length += 1
            lps[i] = length
            i += 1
        else:
            if (length == 0):
                lps[i] = 0
                i += 1
            else:
                length = lps[length - 1]
    i = 0
  
    for k in range(lps[n - 1], m):
        if (b[k] != a[i]):
            return False
        i += 1
    return True
  
if __name__ == "__main__":
  
    s1 = "ABACD"
    s2 = "CDABA"
    print("1" if isRotation(s1, s2) else "0")