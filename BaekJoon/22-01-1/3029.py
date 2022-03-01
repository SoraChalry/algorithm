import sys
input = sys.stdin.readline

s_hh, s_mm, s_ss = map(int, input().split(':'))
f_hh, f_mm, f_ss = map(int, input().split(':'))
r_hh, r_mm, r_ss = 0,0,0

if s_ss > f_ss:
    f_mm -= 1
    r_ss = 60-s_ss+f_ss
else:
    r_ss = f_ss-s_ss

if s_mm > f_mm:
    f_hh -= 1
    r_mm = 60-s_mm+f_mm
else:
    r_mm = f_mm-s_mm

if s_hh > f_hh:
    r_hh = 24-s_hh+f_hh
elif s_hh == f_hh and s_mm == f_mm and s_ss == f_ss:
    r_hh = 24
else:
    r_hh = f_hh-s_hh

r_hh, r_mm, r_ss = map(str, (r_hh, r_mm, r_ss))
print('{}:{}:{}'.format(r_hh.zfill(2), r_mm.zfill(2), r_ss.zfill(2)))