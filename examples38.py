# 10, Fellacy of the Walrus

from math import radians
for angle in range(360):
    print(f'{angle=} {(th:=radians(angle))=:.3f}')

# => angle=0 (th:=radians(angle))=0.000
# => angle=1 (th:=radians(angle))=0.017
# => angle=2 (th:=radians(angle))=0.035
