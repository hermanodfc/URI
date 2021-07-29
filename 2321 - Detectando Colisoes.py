#[ 0,  1,  2,  3]
#[x0, y0, x1, y1]

x0q1, y0q1, x1q1, y1q1 = list(map(int, input().split()))
x0q2, y0q2, x1q2, y1q2 = list(map(int, input().split()))

colisao = 1

if x0q2 > x1q1 or x1q2 < x0q1 or y0q2 > y1q1 or y1q2 < y0q1:
   colisao = 0

print(colisao)
