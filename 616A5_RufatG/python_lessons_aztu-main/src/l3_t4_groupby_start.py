# Dərs 3 · T4 — qruplaşdırma (groupby): region üzrə xülasə
# Əvvəlcə T3 işə salınmalıdır (cells_clean_pd.csv faylını o yaradır).
# İşə salma (de-praktikum qovluğundan): python src/l3_t4_groupby_start.py
import pandas as pd

df = pd.read_csv("data/processed/cells_clean_pd.csv")
print("Sətir:", len(df))

# TODO 1: hər region üçün orta rsrp_dbm:
#         df.groupby("region")["rsrp_dbm"].mean() — round(1) və sort_values() ilə çap

# TODO 2: hər regionda neçə sətir var — df.groupby("region").size()

# TODO 3: iki sütunun ortası birlikdə: cols = ["rsrp_dbm", "throughput_mbps"]
#         rsrp_dbm üzrə sıralayın, çap edin və
#         data/processed/region_summary_pd.csv faylına yazın
