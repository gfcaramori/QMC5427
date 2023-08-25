s_t = int(input("digite o total de segundos: "))
s = 1
h = 3600 * s
m = 60 * s
if s_t < 60:
    print(f'{h * 0}h {m * 0}min {s_t}s')
elif s_t == 60:
    m = s_t//60
    print(f'{h * 0}h {m}min {s_t*0}s')
elif 60 < s_t < 3600:
    m = s_t//60
    s_r = s_t % 60
    print(f'{h * 0}h {m}min {s_r}s')
elif s_t >= 3600:
    h = s_t//3600
    m_r = (s_t % 3600)//60
    s_r = (s_t % 3600) % 60
    print(f'{h}h {m_r}min {s_r}s')
