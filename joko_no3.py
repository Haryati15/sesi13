#. 3 Distribusi penghasilan

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("C:\Users\User\Downloads\dasprog\Data_Penduduk.xlsx")
data.columns = data.columns.str.strip()

def kategori_pengahasilan(nilai):
    if nilai < 1000000:
        return "sangat rendah"
    elif nilai < 2500000:
        return "rendah"
    elif nilai < 5000000:
        return "menengah"
    else:
        return "tinggi"
    
    data["kategori_penghasilan"] = data["penghasilan_per_bulan"].apply(kategori_pengahasilan)
    penghasilan_counts = data["kategori_penghasilan"].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(penghasilan_counts, labels=penghasilan_counts.index, autopct="%1.1f%%", startangle=90, colors=["#ffcc99", "#99ccff", "#ff9999", "#66ff66"])
    plt.title("distribusi penghasilan warga desa cibodas")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
    