# Dərs 3 · Ev tapşırığı — 10 kərpic üzrə 5 mini tapşırıq
# İşə salma (de-praktikum qovluğundan): python src/l3_ev_start.py
# Hər TODO-nun altına kodunuzu yazın. Nəticələr tələbə bələdçisindəki
# və dərs slaydlarındakı nümunələrə oxşardır — ilişsəniz, oraya baxın.
import math

# 1) Dəyişən və hesablama: 0.5 mW gücü dBm-ə çevirin
#    (düstur: dBm = 10 * log10(P, mW); Kərpic 2 və 10)
print("=== 1 ===")
# TODO: power_mw = 0.5, dbm = ..., print(round(dbm, 1))  → -3.0

# 2) Siyahı: 7 gündə düşən zənglərin sayı (Kərpic 5)
print("=== 2 ===")
drops = [3, 0, 5, 1, 0, 2, 4]
# TODO: cəmini (sum), ortasını (sum / len, round ilə) və ən böyüyünü (max) çap edin

# 3) for + if: düşən zəng sayı 2-dən çox olan neçə gün var? (Kərpic 7)
print("=== 3 ===")
# TODO: bad_days = 0; for d in drops: ... ; print("Pis günlər:", bad_days)

# 4) Lüğət: bir baza stansiyasının «pasportu» (Kərpic 6)
print("=== 4 ===")
# TODO: cell = {"cell_id": ..., "region": ..., "band": ...}
# TODO: region-u çap edin, band-ı dəyişin, bütün lüğəti çap edin

# 5) Öz funksiyanız: to_dbm(p_mw) — mW → dBm (Kərpic 8)
print("=== 5 ===")
# TODO: def to_dbm(p_mw): return ...
# TODO: to_dbm(1), to_dbm(0.01), to_dbm(0.000001) çağırıb çap edin

# 6) Öz verilənlər dəstiniz — ayrıca fayl yaradın: src/my_data.py
#    T1 və T4 kimi: read_csv → shape, head, isna().sum() →
#    bir mətn sütunu üzrə groupby və bir ədəd sütununun ortası.
