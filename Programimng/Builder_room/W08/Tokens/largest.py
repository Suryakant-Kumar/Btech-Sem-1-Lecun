# main.py
from tokes2 import TokenSource
def main():
    src = TokenSource([4, 8, 15, 16, 23])
    total = 0
    # ---- WRITE ONLY THIS WHILE LOOP ----
    m = float("-inf")
    while True:
        if src.has_next():
            i = src.next_token()
            m = max(i,m)
        else:
            break
    # ------------------------------------
    print(m)
main()
