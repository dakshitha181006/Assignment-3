
t = int(input())

for _ in range(t):
    n, m, s = map(int, input().split())

    if m <= (n - 1) * (n - 2) // 2 + 1:
        ans = m + s - n + 1

    else:
        core = (n - 1) * (n - 2) // 2

        # Case 1: Unbalanced distribution
        unbalanced = core + (s - n + 2) * (m - core)

        # Case 2: Balanced distribution
        base = s // (n - 1)
        larger = s % (n - 1)
        smaller = n - 1 - larger

        if larger > 0:
            core2 = smaller * (smaller + 1) // 2
            balanced = base * core2 + (base + 1) * (m - core2)
        else:
            balanced = base * m

        # Case 3: Mid-balanced distribution
        midbalanced = base * core + (base + larger) * (m - core)

        ans = min(unbalanced, balanced, midbalanced)

    print(ans)