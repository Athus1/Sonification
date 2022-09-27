import numpy as np
import pandas as pd

overdosedf = pd.read_csv(r"overdose data.csv")
overdosedf = overdosedf.replace(',', '', regex=True)

# print(overdosedf)
#print(overdosedf["Year"])

beats = overdosedf["Year"].count()
#print(beats)

mididict = {'pitch1': [], 'pitch2': [], 'pitch3': [], 'pitch4': [], 'pitch5': [], 'pitch6': []}
mididf = pd.DataFrame(data=mididict)
a = 0
while beats > 0:
    mididf.loc[len(mididf.index)] = [int((overdosedf["Opioids"][a])), int((overdosedf["Heroin"][a])), int((overdosedf["Cocaine"][a])), int((overdosedf["Psychostimulants with abuse potential"][a])), int((overdosedf["Benzodiazepines"][a])), int((overdosedf["Antidepressants"][a]))]
    beats = beats - 1
    a = a + 1

s = mididf.select_dtypes(include=[np.number])
s = ((s-547)/(68630-547))*(8000-0)+0
mididf[s.columns] = s
mididf = mididf.astype(int)
print(mididf)
scale_notes = [64, 66, 67, 69, 71, 72, 75, 76, 78, 79, 81, 83, 84, 87, 88, 90, 91, 93, 95, 96, 99]
