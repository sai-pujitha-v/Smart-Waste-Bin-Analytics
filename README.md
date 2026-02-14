# 🗑️ Smart Waste Bin Analytics

A data-driven infrastructure project that transforms standard waste bins into IoT nodes to optimize collection schedules and monitor urban cleanliness.

## 🚀 Features
- **Fill-Level Tracking:** Real-time distance sensing using Ultrasonic transducers.
- **Collection Forecasting:** Predicts when a bin will overflow based on historical fill rates.
- **Route Optimization:** Identifies which bins require immediate attention to save fuel and time.
- **Dynamic WiFi Config:** Easy deployment via Serial Monitor provisioning.

## ⚙️ Engineering Logic
- **Hardware:** ESP32 uses an HC-SR04 Ultrasonic sensor to measure the distance from the lid to the trash.
- **Software:** Python converts distance into a percentage ($Fill\% = \frac{TotalHeight - Distance}{TotalHeight} \times 100$) and visualizes the urgency level.
