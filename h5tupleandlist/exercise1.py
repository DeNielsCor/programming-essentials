List = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print(f"Original list: {List}")
List[0], List[-1] = List[-1], List[0]
print(f"After the switch: {List}")