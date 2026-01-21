# Sensor Data Analysis for Predictive Insight

## Problem Statement
Modern vehicles generate continuous sensor data such as temperature,
vibration, and RPM. Analyzing this data helps detect abnormal behavior
early and supports predictive maintenance.

## Objective
- Simulate realistic vehicle sensor data
- Analyze trends and statistical patterns
- Identify abnormal behavior using basic data analysis
- Provide engineering insights based on observations

## Tools Used
- Python
- NumPy
- Matplotlib

## Data Analysis & Observations

### Sensor Behavior Analysis

- **RPM Sensor**  
  The RPM signal remains mostly stable during normal operation.
  Sudden spikes were observed during specific time intervals,
  indicating abnormal engine behavior.

- **Temperature Sensor**  
  The temperature signal shows gradual variation over time.
  Any sudden rise beyond the normal operating range can indicate
  potential overheating conditions.

- **Vibration Sensor**  
  Vibration data shows increased fluctuations during abnormal periods.
  High vibration levels may indicate mechanical imbalance or wear.

- **Tyre Pressure Sensor**  
  Tyre pressure remains relatively stable with minor fluctuations.
  Sudden drops or spikes could indicate leakage or sensor malfunction.

### Statistical Insights

Basic statistical analysis was performed using mean and standard deviation:

- Sensors showing abnormal behavior had higher standard deviation,
  indicating larger fluctuations.
- Statistical metrics helped confirm visual observations from plots.
- This approach demonstrates how simple analytics can support
  early fault detection.

## Real-World Relevance

This project demonstrates a simplified version of predictive maintenance
used in the automotive industry. By analyzing time-series sensor data,
potential faults can be detected early, reducing maintenance costs and
preventing system failures.

The same approach can be extended using machine learning and deep learning
models for automated fault detection.



