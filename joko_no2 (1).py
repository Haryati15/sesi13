#. 2 perbandingan pendidikan dan jenis kelamin

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:\Users\User\Downloads\dasprog\Data_Penduduk.xlsx")
grouped = data.groupby(["pendidikan_terakhir", "jenis_kelamin"]).size().unstack(fill_value=0)

grouped.plot(kind="bar", figsize=(10, 6))
plt.title("perbadingan pendidikan terakhir dan jenis kelamin")
plt.xlabel("pendidikan terakhir")
plt.ylabel("jumlah warga")
plt.xticks(rotation=40)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.legend(title="jenis kelamin")
plt.tight_layout()
plt.show()