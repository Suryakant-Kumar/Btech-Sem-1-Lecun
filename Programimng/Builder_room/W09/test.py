# Write your code here
goal = int(input())
days = 0
highest = [1,0]
streak = 0
while True:
    m = int(input())
    if m == -1:
        break
    else:
        days +=1
        if goal <= m:
            print(f"Day {days}: {m} steps - Goal met")
            streak +=1
        else:
            print(f"Day {days}: {m} steps - Goal missed")
        if highest[1]<m:
            highest = [days,m]
print(f"Days goal met: {streak} out of {days}")
print(f"Best day: Day {highest[0]} with {highest[1]} steps")

