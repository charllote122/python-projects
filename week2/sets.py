set1=input("Enter integers for set 1 (space-separated): ").split()
set2=input("Enter integers for set 2 (space-separated): ").split()

set1 = set(map(int, set1))
set2 = set(map(int, set2))
common = set1 & set2
print("Common elements:", common)