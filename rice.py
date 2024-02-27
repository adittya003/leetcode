def max_bags_sold(n, m, customers, bags):
    customers.sort(key=lambda x: (x[1], x[0]), reverse=True)
    bags.sort(key=lambda x: (x[1], x[0]), reverse=True)

    bags_sold = 0
    bag_index = 0

    for customer in customers:
        q, p = customer

        while bag_index < m and (bags[bag_index][1] > p or bags[bag_index][0] < q):
            bag_index += 1

        if bag_index < m:
            bags_sold += 1
            bag_index += 1

    return bags_sold

# Reading input
n, m = map(int, input().split())
customers = [list(map(int, input().split())) for _ in range(n)]
bags = [list(map(int, input().split())) for _ in range(m)]

# Output
result = max_bags_sold(n, m, customers, bags)
print(result)
