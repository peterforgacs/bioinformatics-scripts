
pattern = "ATGATCAAG"
k = len(pattern)

for i in range (len(s)):
    if s[i:i+k] == pattern:
        print i,
