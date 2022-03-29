from random import randint

def create_test_case(cities, ballots, max_population):
    s = [f"{cities} {ballots}"]
    for _ in range(cities):
        pop = randint(1, max_population)
        s.append(f"{pop}")
    s.append("")
    return "\n".join(s)

print(create_test_case(5, 10, 10000))
print("-1 -1")
