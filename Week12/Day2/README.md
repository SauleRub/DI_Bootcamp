Summary & Insights

🔹 Data Overview

We analyzed over 10,000 trading days of Apple Inc. stock data spanning from 1981 to 2023. The dataset included daily open, high, low, close, adjusted close, and volume figures.

🔹 Key Findings
	1.	No Missing Values:
	•	Data was complete and well-structured, with all key columns intact.
	2.	Price Trends:
	•	Apple stock showed steady growth after 2005, with rapid acceleration after 2019.
	•	Volume peaked during major market events (e.g., early 2000s, 2008 crash, COVID period).
	3.	Moving Averages:
	•	30-day moving averages effectively smoothed short-term noise and highlighted long-term trends.
	4.	Hypothesis Testing:
	•	We compared the average closing prices of 2000 vs. 2022.
	•	The t-test showed an extremely small p-value (p < 0.0001), meaning the price increase over time is statistically significant.
	5.	Daily Returns:
	•	Daily returns showed a near-normal bell-shaped distribution, but with some outliers.
	•	This implies Apple stock is generally stable, but not free from large market shocks.
	6.	Correlation (Advanced):
	•	Weak negative correlation (-0.21) between 30-day MA and trading volume.
	•	Suggests rising average prices might slightly coincide with reduced trading volume, but the relationship is not strong.

⸻

💬 Reflection

✅ Challenges Faced
	•	CSV file formatting: The dataset had spaces in column names and ambiguous date formatting, requiring cleaning and formatting before analysis.
	•	Plot clarity: With over 10,000 points, plots were initially cluttered. Formatting and subplot strategies helped improve readability.

✅ What I Learned
	•	How to apply rolling averages using both Pandas and NumPy’s convolve.
	•	How to perform t-tests and normality checks using SciPy.
	•	How to visualize financial data trends effectively over time.
	•	How to interpret correlation in the context of trading metrics.
