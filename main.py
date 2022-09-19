import pandas as pd

overdosedf = pd.read_csv(r"C:\Users\athar\Documents\Python Scripts\overdose data.csv")
overdosedf = overdosedf.replace(',', '', regex=True)

#print(overdosedf)
#print(overdosedf["Year"])


beats = overdosedf["Year"].count() - 1
print(beats)

