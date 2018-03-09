from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import sys

def count_and_clean(data):
    with open(data, 'r') as f:
        data = [line.rstrip('\n') for line in f]
        c = Counter()
        for line in data:
            c.update(line.split())
    
    # removing stopwords
    sw = stopwords.words('english')
    sw.extend(("like", "I", "if", "i'm", "I'm", "The", "I've", "If", "would", "*"))
    for key in sw:
        del c[key]

    return c

def generate_cloud(d):
    wordcloud = WordCloud()
    wordcloud.generate_from_frequencies(frequencies=d)
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    c = count_and_clean(sys.argv[1])
    print('Data counted and cleaned.. generating cloud..')
    generate_cloud(c)
