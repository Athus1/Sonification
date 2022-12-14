import pandas as pd
import matplotlib.pyplot as plt

overdosedf = pd.read_csv(r"C:\Users\athar\PycharmProjects\Sonification\overdose data.csv")
overdosedf = overdosedf.replace(',', '', regex=True)

plt.plot(overdosedf["Year"], (overdosedf["All"]), label="All")
plt.plot(overdosedf["Year"], (overdosedf["Opioids"]), label="Opiods")
plt.plot(overdosedf["Year"], (overdosedf["Heroin"]), label="Heroin")
plt.plot(overdosedf["Year"], (overdosedf["Cocaine"]), label="Cocaine")
plt.plot(overdosedf["Year"], (overdosedf["Psychostimulants with abuse potential"]), label="Psychostimulants with abuse potential")
plt.plot(overdosedf["Year"], (overdosedf["Benzodiazepines"]), label="Benzodiazepines")
plt.plot(overdosedf["Year"], (overdosedf["Antidepressants"]), label="Antidepressants")
plt.title('Drug Overdose Deaths over time')
plt.xlabel('Year')
plt.ylabel('ODs')
plt.grid(True)
plt.legend()
plt.show()