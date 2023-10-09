num_lines = int(input())
words = set()

for _ in range(num_lines):
    line = input().split()
    words.update(line)
    
print(len(words))
