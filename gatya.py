import numpy as np
import random

#random = random.randint(1, 100)

for i in range(10):
    print(np.random.choice(["Rank5 servant","Rank4 servant","Rank3 servant",
                            "Rank5 reisou","Rank4 reisou","Rank3 reisou"],
                         p=[0.01, 0.03, 0.04, 0.12, 0.4, 0.4]))
