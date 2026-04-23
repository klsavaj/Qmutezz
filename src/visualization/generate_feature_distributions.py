import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_parquet("data/simulated/candidate_pairs.parquet")

# Select key features for visualization
features = ['detour_distance_km', 'overlap_ratio', 'time_diff_mins', 
            'driver_approx_fare', 'rider_approx_fare', 'fare_ratio']
feature_labels = ['Detour (km)', 'Overlap Ratio', 'Time Diff (min)',
                  'Driver Fare ($)', 'Rider Fare ($)', 'Fare Ratio']

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 7))
axes = axes.flatten()

# Plot each feature
for idx, (feat, label) in enumerate(zip(features, feature_labels)):
    ax = axes[idx]
    
    # Separate by label
    accepted = df[df['label'] == 1][feat]
    rejected = df[df['label'] == 0][feat]
    
    # Plot overlapping histograms
    ax.hist(rejected, bins=30, alpha=0.6, color='#fc8d62', label='Rejected', density=True)
    ax.hist(accepted, bins=30, alpha=0.6, color='#66c2a5', label='Accepted', density=True)
    
    ax.set_xlabel(label)
    ax.set_ylabel('Density')
    
    # Only show legend on first subplot
    if idx == 0:
        ax.legend()


fig.tight_layout()
os.makedirs("figures", exist_ok=True)
fig.savefig("figures/feature_distributions.png", dpi=150)
plt.close(fig)
print("Saved figures/feature_distributions.png")