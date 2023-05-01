import os
import pandas as pd
from sklearn.linear_model import LinearRegression

path = input("Input path to directory that you want to analyze: ")
averages = []

for filename in os.listdir(path):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(path, filename))
        avg = df['Viewer Count'].mean()
        averages.append(avg)

X = [[i] for i in range(len(averages))]
y = averages

# Train the linear regression model
reg = LinearRegression().fit(X, y)

next_avg = reg.predict([[len(averages)]])[0]

print(f"The predicted average of the next CSV file is: {next_avg}")
