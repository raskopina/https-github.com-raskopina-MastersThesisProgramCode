import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Данные
data = {
    'Augmentation': ['Без искажений', 'Rotation', 'Rotation', 'Rotation', 'Rotation', 'Rotation', 'Width_Shift', 'Width_Shift', 'Width_Shift', 'Width_Shift', 'Width_Shift', 'Height_Shift', 'Height_Shift', 'Height_Shift', 'Height_Shift', 'Height_Shift', 'Shear', 'Shear', 'Shear', 'Shear', 'Shear', 'Zoom', 'Zoom', 'Zoom', 'Zoom', 'Zoom', 'Horizontal_Flip', 'Brightness', 'Brightness', 'Brightness', 'Brightness', 'Brightness', 'Channel_Shift', 'Channel_Shift', 'Channel_Shift', 'Channel_Shift', 'Channel_Shift'],
    'Intens': ['-', 10, 20, 30, 40, 50, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0.5, 'True', '(0.8, 1.2)', '(0.7, 1.3)', '(0.6, 1.4)', '(0.5, 1.5)', '(0.4, 1.6)', 10, 20, 30, 40, 50],
    'Accuracy': [0.937, 0.875, 0.841, 0.794, 0.785, 0.748, 0.897, 0.862, 0.851, 0.833, 0.818, 0.907, 0.921, 0.913, 0.895, 0.879, 0.935, 0.931, 0.915, 0.910, 0.918, 0.847, 0.831, 0.802, 0.778, 0.758, 0.932, 0.939, 0.931, 0.923, 0.919, 0.900, 0.935, 0.927, 0.921, 0.913, 0.902],
    'Recall': [0.956, 0.979, 0.992, 0.987, 0.989, 0.994, 0.966, 0.959, 0.966, 0.974, 0.979, 0.976, 0.982, 0.987, 0.984, 0.979, 0.969, 0.971, 0.974, 0.976, 0.976, 0.984, 0.976, 0.987, 0.974, 0.987, 0.938, 0.966, 0.969, 0.959, 0.961, 0.964, 0.961, 0.964, 0.964, 0.966, 0.969],
    'Precision': [0.944, 0.845, 0.801, 0.757, 0.748, 0.714, 0.880, 0.842, 0.824, 0.801, 0.784, 0.886, 0.901, 0.887, 0.866, 0.850, 0.931, 0.922, 0.898, 0.890, 0.900, 0.811, 0.798, 0.765, 0.748, 0.725, 0.953, 0.937, 0.924, 0.921, 0.914, 0.886, 0.937, 0.918, 0.910, 0.898, 0.879],
    'F1 мера': [0.950, 0.907, 0.886, 0.857, 0.852, 0.831, 0.921, 0.896, 0.890, 0.879, 0.871, 0.929, 0.939, 0.934, 0.922, 0.910, 0.949, 0.946, 0.934, 0.931, 0.937, 0.889, 0.878, 0.862, 0.846, 0.836, 0.945, 0.952, 0.946, 0.939, 0.937, 0.923, 0.949, 0.940, 0.936, 0.931, 0.922],
    'ROC AUC': [0.982, 0.975, 0.972, 0.962, 0.957, 0.908, 0.960, 0.956, 0.945, 0.944, 0.941, 0.979, 0.981, 0.980, 0.978, 0.969, 0.984, 0.983, 0.982, 0.982, 0.983, 0.961, 0.945, 0.946, 0.926, 0.899, 0.981, 0.983, 0.979, 0.979, 0.979, 0.971, 0.981, 0.979, 0.979, 0.978, 0.973],
    'PR AUC': [0.989, 0.985, 0.983, 0.976, 0.972, 0.941, 0.976, 0.975, 0.968, 0.967, 0.966, 0.986, 0.987, 0.986, 0.981, 0.972, 0.990, 0.990, 0.989, 0.990, 0.990, 0.977, 0.960, 0.966, 0.950, 0.923, 0.988, 0.990, 0.985, 0.988, 0.986, 0.981, 0.988, 0.985, 0.987, 0.986, 0.982],
    'Log Loss': [0.212, 0.465, 0.757, 0.986, 1.088, 1.414, 0.525, 0.590, 0.662, 0.716, 0.821, 0.377, 0.380, 0.409, 0.411, 0.534, 0.224, 0.247, 0.278, 0.286, 0.278, 0.735, 1.019, 1.231, 1.372, 1.840, 0.228, 0.226, 0.259, 0.265, 0.263, 0.377, 0.237, 0.244, 0.253, 0.268, 0.308]
}

df = pd.DataFrame(data)

# Столбчатые диаграммы для каждой метрики
metrics = ['Accuracy', 'Recall', 'Precision', 'F1 мера', 'ROC AUC', 'PR AUC', 'Log Loss']

fig, axs = plt.subplots(len(metrics), 1, figsize=(12, 35))
colors = sns.color_palette("husl", len(df['Augmentation'].unique()))

for i, metric in enumerate(metrics):
    sns.barplot(x='Intens', y=metric, hue='Augmentation', data=df, ax=axs[i], palette=colors)
    axs[i].set_title(metric)
    axs[i].set_xlabel('Intensity')
    axs[i].set_ylabel(metric)
    axs[i].legend(loc='upper right')
    axs[i].grid(True)

plt.tight_layout()
plt.show()

# Тепловая карта
plt.figure(figsize=(12, 10))
pivot_table = df.pivot("Augmentation", "Intens", "Accuracy")
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt=".3f")
plt.title('Тепловая карта Accuracy по аугментациям и интенсивности')
plt.show()