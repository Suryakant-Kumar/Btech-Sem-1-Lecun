READ = 0b100 # 4
WRITE = 0b010 # 2
EXECUTE = 0b001 # 1
perms = READ | WRITE # user can read and write, but not execute
print(bin(perms))
print(bool(perms & READ)) # can the user read?
print(bool(perms & EXECUTE)) # can the user execute?
