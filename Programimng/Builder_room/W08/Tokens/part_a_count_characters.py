# Part A
#
# Count the total number of characters in all the tokens.
#
# Fill in the while loop below. Do not change anything else.

from prompt_tokens import PromptTokens

source = PromptTokens(["I", "reside", "in", "Delhi", "."])
total = 0

# ---- WRITE ONLY THIS WHILE LOOP ----
while True:
    if source.has_next():
        i = source.next_token()
        total+=len(i)
    else:
        break
# ------------------------------------

print(total)
