import math
import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def compare(hm, dm, hc, dc):
    ttk_a = math.ceil(hm / dc)
    ttk_b = math.ceil(hc / dm)
    return ttk_a <= ttk_b

for i in range(1, len(lines), 3):
    health_char, damage_char = map(int, lines[i].split())
    health_monster, damage_monster = map(int, lines[i + 1].split())
    k, w, a = map(int, lines[i + 2].split())
    for on_armor in range(k+1):
        new_health_char = health_char + on_armor * a
        new_damage_char = damage_char + (k - on_armor) * w
        if compare(health_monster, damage_monster, new_health_char, new_damage_char):
            print("YES")
            break
    else:
        print("NO")
    # print(compare(health_monster, damage_monster, health_char, damage_char))