E, S, M = tuple(map(int, input().split()))

(e_count, s_count, m_count) = (0, 0, 0)
(E_MAX, S_MAX, M_MAX) = (15, 28, 19)
counter = 0

while True:
    counter += 1
    e_count += 1
    s_count += 1
    m_count += 1
    if e_count > E_MAX:
        e_count = 1
    if s_count > S_MAX:
        s_count = 1
    if m_count > M_MAX:
        m_count = 1
    if e_count == E and s_count == S and m_count == M:
        break
print(counter)
