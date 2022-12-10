print("# Advent of Code - Day 1 #\n")

with open("input.txt", "r") as f:
    rations = f.readlines()

id = 1
ration_log = dict()
ration_total_log = dict()
top_elf_rations = list()
heaviest_elf = None
heaviest_amount = 0

# Create dict holding lists of each elf's rations
for ration in rations:
    if f"elf_{id}" not in ration_log:
        ration_log[f"elf_{id}"] = list()
    try:  
        ration_log[f"elf_{id}"].append(int(ration))
    except:
        id += 1

# Add elf ration values together and determine largest ration holder
for elf, elf_rations in ration_log.items():
    ration_amount = sum(elf_rations)
    ration_total_log[elf] = ration_amount
    if ration_amount > heaviest_amount:
        heaviest_elf = elf
        heaviest_amount = ration_amount
print(f"Heaviest elf is {heaviest_elf} at {heaviest_amount} calories!")
sorted_ration_totals = sorted(ration_total_log.items(), key=lambda x:x[1])

# Calculate top 3 ration holders
print("\nTop 3 elves:")
for k,v in sorted_ration_totals[-3:]:
    top_elf_rations.append(v)
    print(f" - {k} at {v} calores")

print(f"\nTotal amount of top elves: {sum(top_elf_rations)}")
