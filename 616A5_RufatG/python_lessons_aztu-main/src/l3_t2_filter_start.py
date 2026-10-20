# Dərs 3 · T2 — sütun seçirik və filtrləyirik
# İşə salma (de-praktikum qovluğundan): python src/l3_t2_filter_start.py
import pandas as pd

df = pd.read_csv("data/raw/cells_day.csv")

# TODO 1: rsrp_dbm sütununu götürün (lüğətdəki kimi kvadrat mötərizə),
#         ilk 3 dəyəri və ortasını (mean, round ilə) çap edin

# TODO 2: maska — hər sətir üçün True / False: df["rsrp_dbm"] < -105
#         mask.head(3) çap edin

# TODO 3: df[mask] — yalnız zəif ölçmələr; sayını len(...) ilə çap edin

# TODO 4: region "Yasamal" olan sətirlərin sayını çap edin
#         (diqqət: 588 sətir / 6 region ≈ 98 — bəs niyə az çıxdı?)
