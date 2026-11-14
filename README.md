# Inventory & Stockout Optimization: Predictive Modeling

Predicting chronic stockout risk and total inventory holding/shortage costs across 45,000 simulated SKU replenishment cycles using tree-based machine learning models (**Random Forest** and **XGBoost**).

## Problem Statement

Every inventory replenishment decision balances two competing operational costs:
* **Stockouts (Under-buffering):** Lost sales, shortage penalties, and damaged customer goodwill.
* **Overstocking (Over-buffering):** Tied-up working capital, warehousing fees, and spoilage for perishables.

While traditional inventory policies size safety stock buffers around **demand variability**, ~55% of policies ignore **supplier lead-time variability**. When supplier lead times fluctuate unpredictably, demand-only safety buffers fail—causing chronic stockouts even when demand is stable.

This project uses machine learning to predict which SKUs will experience chronic stockouts (`stockout_occurred`) and estimate total replenishment costs (`total_cost`), enabling data-driven safety stock and service-level optimization.

---

## Dataset Overview

* **Source:** [Kaggle — Inventory & Stockout Optimization](https://www.kaggle.com/datasets/sergionefedov/inventory-and-stockout-optimization) (`sergionefedov/inventory-and-stockout-optimization`)
* **Size:** 45,000 SKU replenishment profiles across 28 features.
* **Generation Methodology:** 100% synthetic dataset generated via Monte-Carlo simulation calibrated to supply chain theory (dual-variability safety stock, critical-ratio service levels, and nonlinear service-level cost tails).

### Key Features & Targets
* **Demand & Supply Inputs:** `mean_daily_demand`, `sigma_daily_demand`, `demand_cv`, `mean_lead_time`, `sigma_lead_time`, `lead_time_cv`, `category`.
* **Cost & Policy Parameters:** `unit_cost`, `holding_rate_annual`, `stockout_penalty`, `order_cost`, `target_service_level`, `safety_stock`, `reorder_point`, `order_quantity`.
* **Primary Modeling Targets:**
  * `stockout_occurred` *(Binary Classification)*: Whether the SKU chronically stocks out ($\ge 20\%$ of cycles).
  * `total_cost` *(Regression)*: Total simulated inventory cost combining holding and shortage costs.

---

## Project Structure

```text
mid_term
        ├── midterm.ipynb   # EDA, feature engineering, model training & evaluation
        ├── .gitignore               # Excludes local caches, virtual environments, and raw CSVs
        └── README.md                # Project documentation
