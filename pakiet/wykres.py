import calculations as cl  # najezdzamy kursorem na nazwe biblioteki (calculation), czekamy i jak pojawi sie polecenie import to importujemy, to as to tylko alias

def wykres():
    cl.plotfunc("x**2", start=0, end=2, points=3)

def wykres2():
    cl.plotfunc("x**2 + 10", start=0, end=2, points=3)