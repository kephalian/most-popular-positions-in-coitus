
import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

# Create a dictionary from the given data
data = {
    'Position': ['Doggy', 'Missionary', 'Cowgirl', 'Mouth-69', 'Holding legs up', 'Spooning', 'Reverse cowgirl', 'Oral', 'Anal', 'Tabletop'],
    'Percentage': [35.1, 22.5, 19.4, 4.3, 4.3, 4.1, 3.9, 3.2, 2.1, 1.2]
}

# Create a DataFrame
df = pd.DataFrame(data)
# Define colors for each bar
colors = ['red', 'green', 'blue', 'orange', 'yellow', 'grey',
'magenta', 'pink', 'purple', 'cyan']

# Create a colormap with 15 distinct colors
#colors = plt.cm.viridis(np.linspace(0, 1, len(df['Position'])))

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df['Position'], df['Percentage'], color=colors)

#perc=df['Percentage']
# Add percent labels above the bars
for i, value in enumerate(df['Percentage']):
    per=df['Percentage'][i]
    plt.text(i, value + 1, f'{per:.1f}%', ha='center')
    
    
plt.xlabel('Sex Position')
plt.ylabel('Percentage (%)')
plt.title('Most Popular Sex Positions 2000 people were polled')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#```
#pip install pandas matplotlib
#```
