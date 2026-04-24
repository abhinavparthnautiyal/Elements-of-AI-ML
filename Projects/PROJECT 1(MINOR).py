import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image
import requests
from io import BytesIO

# ── Load image ────────────────────────────────────────────────────────────────
IMAGE_URL = "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600"

response = requests.get(IMAGE_URL, headers={"User-Agent": "Mozilla/5.0"})
img = Image.open(BytesIO(response.content)).convert("RGB")
img = np.array(img)

# ── Resize to speed up processing ────────────────────────────────────────────
img_small = cv2.resize(img, (200, 200))
pixels = img_small.reshape(-1, 3)

# ── K-Means Clustering ────────────────────────────────────────────────────────
N_COLORS = 5
kmeans = KMeans(n_clusters=N_COLORS, random_state=42, n_init=10)
kmeans.fit(pixels)

colors = kmeans.cluster_centers_.astype(int)
labels = kmeans.labels_
counts = np.bincount(labels)
percentages = counts / counts.sum() * 100

# ── Sort by dominance ─────────────────────────────────────────────────────────
sorted_idx = np.argsort(-percentages)
colors = colors[sorted_idx]
percentages = percentages[sorted_idx]

# ── RGB → Hex helper ──────────────────────────────────────────────────────────
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)

# ── Plot results ──────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].imshow(img)
axes[0].set_title("Original Image")
axes[0].axis("off")

palette = np.zeros((100, N_COLORS * 100, 3), dtype=np.uint8)
for i, color in enumerate(colors):
    palette[:, i*100:(i+1)*100] = color

axes[1].imshow(palette)
axes[1].set_title("Dominant Colors")
axes[1].axis("off")

for i, (color, pct) in enumerate(zip(colors, percentages)):
    axes[1].text(i*100 + 50, 115, f"{rgb_to_hex(color)}\n{pct:.1f}%",
                 ha='center', fontsize=9)

plt.tight_layout()
plt.show()

# ── Print to console ──────────────────────────────────────────────────────────
print("\nDominant Colors:")
for i, (color, pct) in enumerate(zip(colors, percentages)):
    print(f"  Color {i+1}: {rgb_to_hex(color)} | RGB{tuple(color)} | {pct:.1f}%")