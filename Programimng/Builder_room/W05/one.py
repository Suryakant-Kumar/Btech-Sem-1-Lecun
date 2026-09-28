names = "Python"
scores = [95, 87, 92]
tags = {"Python", "AI", "Beginner","AI"}
print(names[1])
print(scores[1])
# print(tags[1]) # set is immutable you cannot itrate in set
print(tags)
# print(type({}))
# print(type(set()))
l = [1,2,3,4]
l2 = [11,32]
l.append(l2)
print(l)
l2.append(999)
print(l)
print(hash((1, 2, 3)))
# print(hash((1, [2, 3]))) # list is unhashable
# print({1,2,3,[1,2]}) # cant use list as a element in set as list is unhashable but set is
print(hash("Hello"))
# print(hash({'Key':'Value'})) #unhashable
print(type(()))
print(hash(()))
print((1,2,3,[1,2]))
print({(0,0),(1,2)})
# print({(0,0),(1,2,[1,2])})
article_tags = [
{"Python", "AI"},
{"Python", "Web"},
{"AI", "ML"},
]
print(article_tags[0])
print("AI" in article_tags[1])
print(len(article_tags))
