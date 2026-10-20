# Dərs 3 · T3 — təmizləmə: boşlar, region adları, xətalar, dublikatlar
# İşə salma (de-praktikum qovluğundan): python src/l3_t3_clean_start.py
import pandas as pd

df = pd.read_csv("data/raw/cells_day.csv")
print("Oxunan sətir:", len(df))

# TODO 0: hər sütunda boş dəyər sayı — print(df.isna().sum())

# TODO 1: region adları — əvvəl və sonra nunique() çap edin;
#         arada: df["region"] = df["region"].str.strip().str.capitalize()

# TODO 2: mənfi throughput — sayını çap edin, sonra yalnız >= 0 saxlayın

# TODO 3: dublikatlar — df.duplicated().sum() çap edin, sonra drop_duplicates()

# TODO 4: boş rsrp — neçəsi qaldı? (saxlayırıq); len(df.dropna()) ilə müqayisə

# TODO 5: nəticəni yazın — data/processed/cells_clean_pd.csv, index=False
#         və yazılan sətir sayını çap edin (gözlənilən: 572)
