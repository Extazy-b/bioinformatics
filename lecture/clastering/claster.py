import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


def read_csv_to_array(file_path, delimiter=';', has_header=True):
    if has_header:
        df = pd.read_csv(file_path, delimiter=delimiter)
        column_names = df.columns.tolist()
        data_array = df.to_numpy()
    else:
        df = pd.read_csv(file_path, delimiter=delimiter, header=None)
        column_names = None
        data_array = df.to_numpy()
    
    return data_array, column_names


def klastering(data, k = 2):
    data = data.astype(float)
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    while True:
        distances = np.sqrt(((data - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return labels

def visual(data, labels, k=2):
    colors = plt.cm.rainbow(np.linspace(0, 1, k))
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    for i in range(k):
        cluster_points = data[labels == i]
        ax.scatter(
                   cluster_points[:, 0],
                   cluster_points[:, 1],
                   color=colors[i],
                   label=f'Cluster {i+1}',
                   s=50)
    
    ax.set_xlabel('Age')
    ax.set_ylabel('Weight')
    ax.set_zlabel('Height')

    plt.legend()
    plt.grid(True)
    plt.savefig('lecture/clastering/result.png')


if __name__ == "__main__":
    k = 5
    csv_file_path = "lecture/clastering/input.csv"
    data_array, column_names = read_csv_to_array(csv_file_path, delimiter=';', has_header=True)
    labels = klastering(data_array[:, 1:], k)
    visual(data_array[:, 1:], labels, k)
    for data, label in zip(data_array, labels):
        print(f"Name: {data[0]}, Age: {data[1]}, Weight: {data[2]}, Height: {data[3]}, Class: {label}")