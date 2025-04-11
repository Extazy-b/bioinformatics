"""
Perform K-means clustering on a dataset and visualize the results.

This module provides functions to:
- Read CSV files into numpy arrays
- Perform K-means clustering algorithm 
- Visualize clustering results in a 3D scatter plot

Functions:
- read_csv_to_array: Load data from a CSV file into a numpy array
- klastering: Perform K-means clustering on input data
- visual: Create a 3D visualization of clustered data points

The main script demonstrates clustering on age, weight, and height data,
calculating and displaying cluster statistics and visualizations.
"""

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
    print(f"final centroids: \n{centroids}\n")
    return labels, centroids

def visual(data, centroids, labels, k=2):
    colors = plt.cm.rainbow(np.linspace(0, 1, k))
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    for i in range(k):
        cluster_points = data[labels == i]
        ax.scatter(
                   *cluster_points.T.tolist(),
                   color=colors[i],
                   label=f'Cluster {i+1}',
                   s=50)
        ax.scatter(*centroids[i], color=colors[i], s=50, marker='x')

    ax.set_xlabel('Age')
    ax.set_ylabel('Weight')
    ax.set_zlabel('Height')
    return ax


if __name__ == "__main__":
    k = 2
    path = "./lecture/clastering/"
    csv_file_path = "input.csv"

    data_array, column_names = read_csv_to_array(path+csv_file_path, delimiter=';', has_header=True)
    labels, centroids = klastering(data_array[:, 1:], k)
    
    ax = visual(data_array[:, 1:], centroids, labels, k)
    for data, label in zip(data_array, labels):
        print(f"Name: {data[0]}\t\tAge: {data[1]}\tWeight: {data[2]}\tHeight: {data[3]}\tClass: {label}")

    avg = [float(np.mean(col)) for col in data_array.T[1:]]
    median = [float(np.median(col)) for col in data_array.T[1:]]
    var = [float(np.var(col)) for col in data_array.T[1:]]

    print(f"\nAverage:\nAge: {avg[0]:.3}\tWeight: {avg[1]:.3}\tHeight: {avg[2]:.3}")
    print(f"\nMedian:\nAge: {median[0]:.3}\tWeight: {median[1]:.3}\tHeight: {median[2]:.3}")
    print(f"\nVariance:\nAge: {var[0]:.3}\tWeight: {var[1]:.3}\tHeight: {var[2]:.3}")

    ax.scatter(*avg, color='black', label='avg')
    ax.scatter(*median, color='green', label='median')

    plt.legend()
    plt.grid(True)

    plt.savefig(path+"result.png")