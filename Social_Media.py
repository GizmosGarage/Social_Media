import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("C:/Users/ethan/.kaggle/social-media-addiction-vs-relationships/Students_Social_Media_Addiction.csv")

# Set style for appealing visuals
plt.style.use('ggplot')
plt.figure(figsize=(10, 6), facecolor='#f0f0f0')
plt.gca().set_facecolor('#e0e0e0')

# Create scatter plot
sns.scatterplot(data=df, x='Avg_Daily_Usage_Hours', y='Sleep_Hours_Per_Night', hue='Gender', size='Age', palette='viridis', s=100, alpha=0.6)

# Customize
plt.title('Social Media Usage vs Sleep Hours', fontsize=16, pad=20, color='navy')
plt.xlabel('Average Daily Usage (hours)', fontsize=12)
plt.ylabel('Sleep Hours Per Night', fontsize=12)
plt.legend(title='Gender', title_fontsize=12, fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

# Save the plot
plt.savefig('usage_vs_sleep.png', dpi=300, bbox_inches='tight')

plt.show()
