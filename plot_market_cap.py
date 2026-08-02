import matplotlib.pyplot as plt
import numpy as np

# Set dark mode styled background
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), gridspec_kw={'width_ratios': [1, 2.2]})
fig.patch.set_facecolor('#0f172a') # Sleek dark background
for ax in (ax1, ax2):
    ax.set_facecolor('#1e293b')
    ax.spines['bottom'].set_color('#475569')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('#475569')
    ax.tick_params(colors='#e2e8f0', labelsize=10)
    ax.grid(True, color='#334155', linestyle='--', alpha=0.5)

# --- Plot 1: Total Cohort Comparison ---
cohorts = ['MAAMA Group', 'BATMANSS Group']
totals_2020 = [6.25, 1.17]  # in Trillions
totals_2026 = [15.94, 12.61]

x = np.arange(len(cohorts))
width = 0.35

rects1 = ax1.bar(x - width/2, totals_2020, width, label='Mid 2020', color='#0284c7') # Cyan/Blue
rects2 = ax1.bar(x + width/2, totals_2026, width, label='Mid 2026', color='#10b981') # Green

ax1.set_ylabel('Total Market Cap (USD Trillions)', color='#e2e8f0', fontsize=12, fontweight='bold')
ax1.set_title('Group Cohort Growth (Total)', color='#f8fafc', fontsize=14, fontweight='bold', pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(cohorts, color='#e2e8f0', fontsize=11, fontweight='bold')
ax1.legend(facecolor='#1e293b', edgecolor='#475569', labelcolor='#e2e8f0')

# Add values on top of bars
def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'${height:.2f}T',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', color='#f8fafc', fontsize=9, fontweight='bold')

autolabel(rects1, ax1)
autolabel(rects2, ax1)

# --- Plot 2: Individual Company Comparison ---
companies = [
    # MAAMA
    'Apple', 'Alphabet', 'Microsoft', 'Amazon', 'Meta', 'Netflix',
    # Separator / Blank
    '',
    # BATMANSS
    'Nvidia', 'Broadcom', 'Tesla', 'Samsung', 'Micron', 'SK Hynix', 'AMD', 'ASML'
]

# Convert all to Billions for standard comparison on log or linear scale.
comp_2020 = [
    1570, 970, 1470, 1370, 670, 200,
    0, # Separator
    235.2, 123, 223.7, 264, 55.7, 50, 61.1, 152.4
]
comp_2026 = [
    4890, 3900, 2840, 2500, 1510, 298.59,
    0, # Separator
    5010, 1820, 1240, 1120, 1040, 856, 851, 675
]

x_comp = np.arange(len(companies))
width_comp = 0.35

rects_comp1 = ax2.bar(x_comp - width_comp/2, comp_2020, width_comp, label='Mid 2020', color='#0284c7')
rects_comp2 = ax2.bar(x_comp + width_comp/2, comp_2026, width_comp, label='Mid 2026', color='#10b981')

ax2.set_ylabel('Market Cap (USD Billions)', color='#e2e8f0', fontsize=12, fontweight='bold')
ax2.set_title('Individual Company Market Cap (2020 vs 2026)', color='#f8fafc', fontsize=14, fontweight='bold', pad=15)
ax2.set_xticks(x_comp)
ax2.set_xticklabels(companies, rotation=45, ha='right', color='#e2e8f0', fontsize=10)

# Add text labels on top of the bars for visual clarity
for rect in rects_comp1:
    height = rect.get_height()
    if height > 0:
        ax2.annotate(f'${height:,.0f}B' if height < 1000 else f'${height/1000:.1f}T',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(-2, 3), rotation=90,
                    textcoords="offset points",
                    ha='center', va='bottom', color='#94a3b8', fontsize=8)

for rect in rects_comp2:
    height = rect.get_height()
    if height > 0:
        ax2.annotate(f'${height:,.0f}B' if height < 1000 else f'${height/1000:.1f}T',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(2, 3), rotation=90,
                    textcoords="offset points",
                    ha='center', va='bottom', color='#f8fafc', fontsize=8, fontweight='bold')

# Visual demarcation for Groups
ax2.axvline(x=6, color='#475569', linestyle='--', alpha=0.8)
ax2.text(2.5, ax2.get_ylim()[1]*0.9, 'MAAMA Group', color='#38bdf8', ha='center', fontsize=12, fontweight='bold')
ax2.text(10.5, ax2.get_ylim()[1]*0.9, 'BATMANSS Group', color='#34d399', ha='center', fontsize=12, fontweight='bold')

# Layout and save
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, 'assets', 'market_cap_comparison.png')
os.makedirs(os.path.dirname(save_path), exist_ok=True)

plt.suptitle('MAAMA vs. BATMANSS Market Capitalization Growth (2020 vs. 2026)', color='#f1f5f9', fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(save_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
print(f"Plot successfully created and saved to {save_path}")
