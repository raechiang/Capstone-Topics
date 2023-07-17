import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def count_labels(labels, df, print_counts=True):
    """
    Counts the number of articles marked with a label.
    
    labels : A list of column names.
    df : The DataFrame of articles with labels to count.
    print_counts : If set to true, it will print the labels and their occurrences.
    """
    label_count = []
    for label in labels:
        label_sum = df[label].sum()
        label_count.append(label_sum)
        if (print_counts):
            print("{} articles tagged with {}".format(label_sum, label))
    return label_count

def plot_topic_labels(labels, label_count):
    """
    Plots a bar chart for the label counts.
    
    labels : A list of the names of the labels
    label_count : A list of occurrences corresponding to the labels
    """
    _ = plt.figure(figsize=(15,5))
    _ = plt.title("Number of articles per topic")
    _ = plt.bar(labels, label_count)
    _ = plt.xlabel("Topic")
    _ = plt.ylabel("Number of articles")
    _ = plt.show()