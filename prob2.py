import matplotlib.pyplot as G
import pandas as C

df = C.read_csv("data.csv")
df.plot()
G.title("Toate valorile")
G.show()

df[:5].plot()
G.title("Primele cinci valori")
G.show()

df[-11:].plot()
G.title("Ultimele 11 valori")
G.show()