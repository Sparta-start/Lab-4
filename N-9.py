stud = int(input())
lang = set()
one_lang = set()

for _ in range(stud):
    num_lang = int(input())
    stud_lang = set()
    for _ in range(num_lang):
        best_lang = input()
        stud_lang.add(best_lang)
    if not lang:
        lang = stud_lang
    else:
        lang &= stud_lang
    one_lang |= stud_lang

print(len(lang))
for best_lang in sorted(lang):
    print(best_lang)

print(len(one_lang))
for best_lang in sorted(one_lang):
    print(best_lang)
