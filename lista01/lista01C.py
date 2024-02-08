n_bars = int(input())
cost_bars = input().split()
total = 0
for i in range(n_bars):
    cost_bars[i] = int(cost_bars[i])
    total += cost_bars[i]

m_coupons = int(input())
coupons = input().split()

cost_bars.sort()

for q in coupons:
    print(total - cost_bars[n_bars - int(q)])

