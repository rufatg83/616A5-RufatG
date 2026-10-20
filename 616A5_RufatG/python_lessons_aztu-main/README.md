# de-praktikum — Dərs 3

Praktikum: Python ilə data mühəndisliyi (Git, Docker, SQL) · AzTU · 2026/2027 payız

Mövzu: pandas ilə verilənlərin oxunması, təmizlənməsi və çevrilməsi — sıfırdan:
əvvəlcə Python-un 10 «kərpici», sonra eyni kərpiclərlə pandas.

## Qurulma (bir dəfə)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (PowerShell)
source .venv/bin/activate       # macOS / Linux
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Terminal sətrinin əvvəlində `(.venv)` görünməlidir.

## İşə salma

Bütün əmrlər `de-praktikum` qovluğundan (layihə kökündən) yazılır:

```bash
python src/l3_basics_start.py     # Blok 1: Python-un 10 kərpici
python src/l3_t1_read_start.py    # T1: faylı oxu və bax
python src/l3_t2_filter_start.py  # T2: sütun və filtr
python src/l3_t3_clean_start.py   # T3: təmizləmə → data/processed/cells_clean_pd.csv
python src/l3_t4_groupby_start.py # T4: region üzrə qruplaşdırma (əvvəlcə T3!)
python src/l3_ev_start.py         # ev tapşırığı
```

`_start.py` faylları başlanğıc skeletlərdir — `# TODO:` yerlərini dərsdəki slaydlara
baxaraq doldurun. Tam kod dərsdən sonra Teams-də olacaq.

## Gözlənilən nəticələr

- T1: `(588, 6)`; `rsrp_dbm` sütununda 564 dolu dəyər (24 boş)
- T2: orta RSRP −95.9 dBm; zəif ölçmə (< −105 dBm) — 100; `"Yasamal"` — 93 sətir
- T3: region variantı 20 → 6; mənfi throughput 4; dublikat 12; yazılan sətir **572**
- T4: Yasamal −108.7 · Sabunçu −103.1 · Binəqədi −97.4 · Nəsimi −92.5 · Nərimanov −89.4 · Xətai −84.9

## Struktur

- `data/raw/` — xam fayllar (`cells_day.csv`, `cells_meta.json`) — Dərs 2 ilə eyni, dəyişdirilmir
- `data/processed/` — skriptlərin yaratdığı nəticələr (Git-ə düşmür)
- `src/` — kod
