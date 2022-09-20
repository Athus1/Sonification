import pandas as pd

overdosedf = pd.read_csv(r"overdose data.csv")
overdosedf = overdosedf.replace(',', '', regex=True)

# print(overdosedf)
#print(overdosedf["Year"])

beats = overdosedf["Year"].count() - 1
#print(beats)

mididict = {'pitch': [], 'instrument': []}
mididf = pd.DataFrame(data=mididict)
a = 0
while beats > 0:
    mididf.loc[len(mididf.index)] = [overdosedf["Opioids"][a], "test"]
    beats = beats - 1
    a = a + 1
print(mididf)