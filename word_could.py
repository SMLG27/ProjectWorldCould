# Here are all the installs and imports you will need for your word cloud script and uploader widget

#pip install wordcloud
#pip install fileupload
#pip install ipywidgets

#if u use jupyter 
#jupyter nbextension install --py --user fileupload
#jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# This is the uploader widget

def _upload():
    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 ** 10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)



def calculate_frequencies(file_contents):
    listt = []
    word = []
    global result
    result = {}

    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    listt = file_contents.split()
    for word in listt:
        if word not in uninteresting_words:
            for letter in word:
                if letter in punctuations:
                    letter.replace(letter, "")
            if word in result.keys():
                result[word] += 1
            else:
                result[word] = 0

    # wordcloud
    cloud = wordcloud.WordCloud()

    cloud.generate_from_frequencies(result)
    return cloud.to_array()


if __name__ == '__main__':
    _upload()
    # Display your wordcloud image
    file_contents = "Humpty Dumpty is a character in an English nursery rhyme, probably originally a \
    riddle and  one one of the best known in the thethe English-speaking world. He is typically portrayed \
    as an anthropomorphic anthropomorphic anthropomorphicanthropomorphic egg egg egg, though he is not explicitly explicitly explicitly described as such. "
    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation='nearest')
    plt.axis('off')
    plt.show()
