#. 1 visualisasi profesi warga (pie chart)

import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_excel("C:\Users\User\Downloads\dasprog\Data_Penduduk.xlsx")
profesi_count = data["profesi"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(profesi_count, labels=profesi_count.index, autopct="%1.1f%%", startangle=140)
plt.title("presentase profesi warga desa cobodas")
plt.axis("equal")
plt.tight_layout()
plt.show()
