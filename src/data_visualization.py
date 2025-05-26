import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folders if not exist
os.makedirs('figures', exist_ok=True)

# Load the cleaned train dataset
clean_train_df = pd.read_csv('data/processed/cleaned_train.csv')

# Set Seaborn theme
sns.set_theme(style='whitegrid')
def add_value_labels(ax, spacing=5):
    for p in ax.patches:
        if p.get_height() > 0:
            ax.annotate(f'{int(p.get_height())}',
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='bottom',
                        fontsize=9, color='black',
                        xytext=(0, spacing),
                        textcoords='offset points')

def plot_outcome_distribution(df):
    plt.figure(figsize=(6, 4))
    ax = sns.countplot(data=df, x='outcome', hue='outcome', palette='Set2', legend=False)
    add_value_labels(ax)
    plt.title('Outcome Distribution: Human vs Bot', fontsize=14)
    plt.xlabel('Outcome (0 = Human, 1 = Bot)')
    plt.ylabel('Number of Bidders')
    plt.tight_layout()
    plt.savefig('figures/outcome_distribution.png')
    plt.close()
    
plot_outcome_distribution(clean_train_df)