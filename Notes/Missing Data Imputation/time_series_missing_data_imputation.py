# Time-Series Missing Data Imputation – Industry-Grade Notebook
# Focus: Forecasting, Sensors, Finance, Operations
# Goal: Understand WHEN time-series imputation helps and WHEN it silently destroys models

# =========================================================
# 1. Imports
# =========================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression

np.random.seed(42)

# =========================================================
# 2. Generate Realistic Time-Series Data
# =========================================================
# Scenario: Sensor / demand / usage signal

n = 500
trend = np.linspace(10, 25, n)
seasonal = 3 * np.sin(np.arange(n) * 2 * np.pi / 24)
noise = np.random.normal(0, 1, n)

signal = trend + seasonal + noise

df = pd.DataFrame({
    'time': pd.date_range('2023-01-01', periods=n, freq='H'),
    'value': signal
}).set_index('time')

# =========================================================
# 3. Introduce Missingness Patterns
# =========================================================
# 1. Random gaps (MCAR)
# 2. Sensor outage (long block)
# 3. Regime change masking

df_missing = df.copy()

# MCAR
mcar_idx = np.random.choice(n, size=30, replace=False)
df_missing.iloc[mcar_idx, 0] = np.nan

# Sensor outage
outage_start, outage_end = 200, 260
df_missing.iloc[outage_start:outage_end, 0] = np.nan

print('Missing rate:', df_missing.isna().mean().values[0])

# =========================================================
# 4. Visualize Missingness
# =========================================================
plt.figure()
plt.plot(df.index, df['value'], label='True Signal')
plt.plot(df_missing.index, df_missing['value'], label='Observed', linestyle='--')
plt.legend()
plt.title('Time-Series with Missing Blocks')
plt.show()

# =========================================================
# 5. Imputation Strategies
# =========================================================

# Forward Fill
df_ffill = df_missing.fillna(method='ffill')

# Backward Fill
df_bfill = df_missing.fillna(method='bfill')

# Linear Interpolation
df_interp = df_missing.interpolate(method='linear')

# =========================================================
# 6. Compare Imputation Error (Local)
# =========================================================
# Evaluate only on missing positions
mask = df_missing['value'].isna()

mae_ffill = mean_absolute_error(df.loc[mask, 'value'], df_ffill.loc[mask, 'value'])
mae_bfill = mean_absolute_error(df.loc[mask, 'value'], df_bfill.loc[mask, 'value'])
mae_interp = mean_absolute_error(df.loc[mask, 'value'], df_interp.loc[mask, 'value'])

results = pd.DataFrame({
    'Method': ['Forward Fill', 'Backward Fill', 'Interpolation'],
    'MAE_on_Missing': [mae_ffill, mae_bfill, mae_interp]
})

print(results)

# =========================================================
# 7. Forecasting Impact (Hidden Danger)
# =========================================================
# Use lag-1 regression

lag = 1

def make_supervised(series, lag=1):
    X, y = [], []
    for i in range(lag, len(series)):
        X.append(series[i-lag])
        y.append(series[i])
    return np.array(X).reshape(-1, 1), np.array(y)

# Drop NaNs after imputation
X_true, y_true = make_supervised(df['value'].values, lag)
X_imp, y_imp = make_supervised(df_interp['value'].values, lag)

model_true = LinearRegression().fit(X_true, y_true)
model_imp = LinearRegression().fit(X_imp, y_imp)

# Forecast comparison
pred_true = model_true.predict(X_true)
pred_imp = model_imp.predict(X_imp)

print('MAE True:', mean_absolute_error(y_true, pred_true))
print('MAE After Imputation:', mean_absolute_error(y_imp, pred_imp))

# =========================================================
# 8. Key Failure Modes (Very Important)
# =========================================================
# 1. Forward fill assumes stationarity
# 2. Interpolation smooths regime changes
# 3. Long outages create fake stability
# 4. Leakage if future values used

# =========================================================
# 9. Production Rules for Time-Series Imputation
# =========================================================
# DO:
# - Respect temporal order
# - Mark imputed segments
# - Limit gap length

# DON'T:
# - Interpolate across regime shifts
# - Backfill using future info
# - Hide outages from the model

# =========================================================
# 10. Interview-Ready Statements
# =========================================================
# “Interpolation reduces variance but introduces bias.”
# “Long gaps should be modeled, not filled.”
# “Time-series imputation is a forecasting decision.”

# =========================================================
# 11. Exercises
# =========================================================
# 1. Add seasonal interpolation
# 2. Simulate sudden regime shift
# 3. Add missing indicators
# 4. Compare with ARIMA / Prophet
