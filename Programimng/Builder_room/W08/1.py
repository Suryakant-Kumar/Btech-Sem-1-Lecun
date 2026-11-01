n = int(input())

# ── Write your solution here ──
i = 1
while i<=n**0.5:
        if n%i==0:
            if i == n//i:
                count += 1
            else:
                count += 1
        i += 1
