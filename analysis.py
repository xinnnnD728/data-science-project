"""Reproduce the two figures in the CISC7204 data science portfolio.

Data: Gapminder sample distributed with Plotly Express (1952–2007).
Run: python analysis.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)

df = px.data.gapminder()
df = df.dropna(subset=["gdpPercap", "lifeExp"])
df = df[df["gdpPercap"] > 0].copy()

colors = {
    "Africa": "#9A7154",
    "Americas": "#3D83A3",
    "Asia": "#C0713F",
    "Europe": "#6C799B",
    "Oceania": "#6C9B83",
}

# Figure 1: a snapshot in the final year available in this historical sample.
latest = df[df["year"] == 2007]
fig, ax = plt.subplots(figsize=(9, 5.8))
for continent, part in latest.groupby("continent"):
    ax.scatter(
        part["gdpPercap"],
        part["lifeExp"],
        s=np.sqrt(part["pop"] / 1_000_000) * 10,
        alpha=0.67,
        color=colors[continent],
        label=continent,
        edgecolors="white",
        linewidths=0.35,
    )
ax.set_xscale("log")
ax.set_xlabel("GDP per person (US dollars, log scale)")
ax.set_ylabel("Life expectancy at birth (years)")
ax.set_title("Income and life expectancy across countries, 2007")
ax.grid(alpha=0.2)
ax.legend(title="Continent", frameon=False, ncol=2, loc="lower right")
fig.text(
    0.1,
    0.015,
    "Bubble size reflects population on a compressed scale. Data: Gapminder via Plotly Express (CC BY).",
    fontsize=8,
    color="#555555",
)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(OUT / "income_life_expectancy_2007.png", dpi=180)
plt.close(fig)

# Figure 2: the time dimension, using countries featured in earlier class work.
selected = df[df["country"].isin(["China", "India", "United States"])]
fig, ax = plt.subplots(figsize=(9, 5.4))
for country, part in selected.groupby("country"):
    ax.plot(part["year"], part["lifeExp"], marker="o", markersize=3, label=country)
ax.set_xlabel("Year")
ax.set_ylabel("Life expectancy at birth (years)")
ax.set_title("Life expectancy in China, India and the United States, 1952–2007")
ax.grid(alpha=0.2)
ax.legend(frameon=False)
fig.text(
    0.1,
    0.015,
    "Source: Gapminder sample via Plotly Express (CC BY). Historical data end in 2007.",
    fontsize=8,
    color="#555555",
)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(OUT / "life_expectancy_three_countries.png", dpi=180)
plt.close(fig)

print(f"Rows analysed: {len(df)}")
print(f"2007 countries: {latest['country'].nunique()}")
print(f"2007 correlation, log GDP per person vs life expectancy: "
      f"{np.corrcoef(np.log10(latest['gdpPercap']), latest['lifeExp'])[0, 1]:.3f}")
for country in ["China", "India", "United States"]:
    part = selected[selected["country"] == country].sort_values("year")
    print(f"{country}: {part.iloc[0]['lifeExp']:.1f} → {part.iloc[-1]['lifeExp']:.1f} years")
