import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df = pd.read_csv('data/exam.data.csv')

#Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(df['Student'], df['Math'], color='blue', alpha=0.7)
plt.xlabel('Student Name')
plt.ylabel('Math Score')
plt.title('Math Scores of each Students')
plt.tight_layout()
plt.savefig('output/bar_chart.png')
plt.show()