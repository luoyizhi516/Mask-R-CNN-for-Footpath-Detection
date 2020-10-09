import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 101)
y1 = np.array([2.0275, 1.3403, 1.2869, 1.2586, 1.2544, 1.1710, 1.2073, 1.1080, 1.0888, 1.1016,
               1.1035, 1.1115, 1.1072, 1.0988, 1.1573, 1.0797, 1.0653, 1.2324, 1.0406, 1.0676,
               1.0595, 1.0244, 0.9539, 0.9385, 0.9459, 0.8576, 0.8398, 0.6896, 0.5124, 0.4416,
               0.4614, 0.4057, 0.4090, 0.3275, 0.3010, 0.2659, 0.3208, 0.2763, 0.2613, 0.3992,
               0.2382, 0.2685, 0.2208, 0.2559, 0.2698, 0.3803, 0.2501, 0.3032, 0.2332, 0.2287,
               0.2597, 0.2271, 0.2513, 0.2423, 0.2793, 0.2943, 0.2359, 0.2347, 0.2419, 0.2352,
               0.2487, 0.2285, 0.2243, 0.2269, 0.3198, 0.2209, 0.2293, 0.2676, 0.2570, 0.1993,
               0.2025, 0.2839, 0.2340, 0.2196, 0.2200, 0.2074, 0.2969, 0.2124, 0.2256, 0.2202,
               0.2019, 0.2418, 0.2417, 0.1971, 0.2456, 0.2791, 0.2075, 0.1911, 0.3073, 0.2057,
               0.3306, 0.2205, 0.1990, 0.2412, 0.2131, 0.2130, 0.2054, 0.2139, 0.1806, 0.2638])

y2 = np.array([1.1975, 1.5246, 1.6720, 1.0307, 2.0450, 1.4876, 1.6470, 1.3457, 1.2694, 0.9119,
               1.2309, 0.9741, 1.1774, 0.9607, 1.1104, 0.9495, 1.1197, 1.5767, 0.9331, 1.0331,
               0.9585, 0.8850, 0.7940, 0.7449, 0.8640, 0.8233, 0.7569, 0.5938, 1.1827, 2.9812,
               0.1792, 0.3477, 0.4401, 0.1192, 0.1964, 0.0609, 0.1191, 0.3532, 0.3952, 0.2848,
               0.2828, 0.1980, 0.1343, 0.2237, 0.1813, 0.1043, 2.4295, 1.0377, 0.1507, 0.1447,
               0.2426, 0.2068, 0.3295, 0.2618, 0.1882, 0.3137, 0.2293, 0.1991, 0.1370, 0.1651,
               0.1332, 0.0626, 0.0972, 2.3057, 0.1570, 0.1774, 0.1107, 0.1363, 0.1304, 0.1968,
               0.2386, 0.1890, 0.2552, 0.1366, 0.1249, 0.0980, 0.1020, 0.2675, 0.1201, 0.1313,
               0.1838, 0.1453, 0.0695, 0.0552, 0.4836, 0.1350, 0.2554, 0.2621, 0.2380, 0.3306,
               0.1102, 0.1768, 0.1470, 0.0413, 0.1183, 0.1980, 0.1295, 0.3327, 0.1947, 0.0247])

plt.plot(x, y1, color="r", linestyle="-", linewidth=1, label="Loss")  # Loss
plt.plot(x, y2, color="b", linestyle="-", linewidth=1, label="val_loss")  # val_loss
plt.legend(loc='best')

plt.xlabel("Epochs")
plt.ylabel("Loss")

plt.show()