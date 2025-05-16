import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("C:/Users/ethan/.kaggle/social-media-addiction-VS-relationships/Students_Social_Media_Addiction.csv")

# Set style for appealing visuals
plt.style.use('ggplot')
plt.figure(figsize=(12, 6), facecolor='#f0f0f0')
plt.gca().set_facecolor('#e0e0e0')

# Create box plot
sns.boxplot(data=df, x='Most_Used_Platform', y='Sleep_Hours_Per_Night', palette='pastel', width=0.5)
sns.swarmplot(data=df, x='Most_Used_Platform', y='Sleep_Hours_Per_Night', color='black', size=4, alpha=0.5)

# Customize
plt.title('Sleep Hours by Social Media Platform', fontsize=16, pad=20, color='darkgreen')
plt.xlabel('Social Media Platform', fontsize=12)
plt.ylabel('Sleep Hours Per Night', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)

# Save the plot
plt.savefig('platform_vs_sleep.png', dpi=300, bbox_inches='tight')