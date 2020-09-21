from tqdm import tqdm
import time
for i in tqdm(range(0,20),desc="First Loop"):
    for j in tqdm(range(0,5),desc="Second Loop"):
        time.sleep(0.1)

