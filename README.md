# Income and life expectancy: a historical data-visualization project

## Question

How did life expectancy vary with GDP per person across countries in 2007, and how did life expectancy change in China, India, and the United States between 1952 and 2007?

This project develops a question from my CISC7204 visualization practice into a small, reproducible analysis. It is a **historical** comparison, not a picture of current conditions.

## Data source and permission

The script uses `plotly.express.data.gapminder()`, a sample of Gapminder country-level data supplied with Plotly Express. It contains observations every five years from 1952 through 2007. Gapminder says its data may be reused with attribution under a CC BY license. Attribution: **Based on free data from [Gapminder.org](https://www.gapminder.org/data/), CC BY license**, accessed through Plotly Express. No private or course-restricted dataset is uploaded here.

The data and source information can be reviewed at [Gapminder's data page](https://www.gapminder.org/data/) and [Plotly's dataset repository](https://github.com/plotly/datasets/blob/master/gapminderDataFiveYear.csv).

## Method

1. Load the Gapminder sample with Plotly Express and remove missing or non-positive GDP-per-person values.
2. For 2007, plot GDP per person against life expectancy. Use a logarithmic horizontal scale because incomes span a wide range; colour countries by continent and use a compressed population scale for bubble size.
3. Plot life expectancy over time for China, India, and the United States.
4. Calculate the Pearson correlation between log GDP per person and life expectancy in 2007. This is a description of association, not a causal estimate.

Tools: Python, Plotly Express (for the included sample data), NumPy, and Matplotlib.

## Key findings

- Higher GDP per person and longer life expectancy tend to occur together in the 2007 sample. The correlation between log GDP per person and life expectancy is **0.809** across 142 countries, but points still vary substantially at similar income levels.
- All three selected countries gained years of life expectancy between 1952 and 2007: China from about **44.0 to 73.0**, India from **37.4 to 64.7**, and the United States from **68.4 to 78.2**. Their trajectories differed, which a single 2007 scatter plot would hide.

The figures are in [`figures/`](figures/):

![GDP per person and life expectancy in 2007](figures/income_life_expectancy_2007.png)

![Life expectancy in three countries](figures/life_expectancy_three_countries.png)

## Limitation

The sample ends in 2007 and does not describe today's outcomes. National averages conceal differences within countries. The positive association does not show that income alone caused longer lives; health systems, education, public policy, and other factors also matter.

## Reproduce the analysis

From this repository's root folder:

```bash
python -m pip install -r requirements.txt
python analysis.py
```

The script saves two PNG figures in `figures/` and prints summary statistics. The required dataset is included in Plotly Express, so no separate download or API key is needed.
