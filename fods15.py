from collections import Counter
import matplotlib.pyplot as plt

def calculate_likes_frequency(like_counts):
    return Counter(like_counts)

def plot_likes_frequency(freq_dist):
    likes, frequencies = zip(*freq_dist.items())

    plt.bar(likes, frequencies)
    plt.xlabel('Number of Likes')
    plt.ylabel('Frequency')
    plt.title('Frequency Distribution of Likes')
    plt.show()

if __name__ == "__main__":
        
    sample_likes_list = [10, 20, 10, 5, 30, 10, 20, 10, 15, 25, 30, 20, 10]

    freq_dist = calculate_likes_frequency(sample_likes_list)
    print("Likes Frequency Distribution:")
    print(freq_dist)

    plot_likes_frequency(freq_dist)
    '''
Likes Frequency Distribution:
Counter({10: 5, 20: 3, 30: 2, 5: 1, 15: 1, 25: 1})
'''
