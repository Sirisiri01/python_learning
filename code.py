import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
data = {
    "Hours_Studied": [2,3,5,7,9],
     "Test_Score": [55,60,75,85,95],
        "Hours_Playing_Games": [5,5,2,1,0]
}
df = pd.DataFrame(data)
# print(df)
corr_matrix = df.corr()
print(corr_matrix)

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix,annot=True,camp="coolwarm", fmt=".2f")
plt.title("correlation Matrix Heatmap")
plt.show()
