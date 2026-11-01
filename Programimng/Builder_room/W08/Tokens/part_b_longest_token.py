# Part B
#
# Find the longest token and print it.
#
# Fill in the while loop below. Do not change anything else.

from prompt_tokens import PromptTokens

source = PromptTokens(["I", "reside", "in", "Delhi", "."])
longest = ""

# ---- WRITE ONLY THIS WHILE LOOP ----
i = ""
while True:
    if source.has_next():
        i = source.next_token()
        if len(longest)<len(i):
            longest = i
    else:
        break    

# ------------------------------------

print(longest)
