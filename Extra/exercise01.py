import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'Records.csv'
data = pd.read_csv(csv_file)
countries = data['country']

pychart = data['country'].value_counts().head().plot(kind='pie', figsize = (10, 8))
pychart.set_title("Distribution by Country")

plt.legend()
plt.show()

plt.savefig('piechart.png')