# Imported modules for word cloud project
import wordcloud
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io

# =========== NOTICE ===========

# Almost all of this code is taken
# right from Jupyter notebook
# Real project begins later

# upload widget saves contents
# of uploaded file into a string
# named file_contents
# These lines of code are mainly used
# for uploading from device to browser

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))

        filename = change['owner'].filename
        print('Uploaded `{}` ({:2f} kB'.format(
            filename, len(decoded.read()) / 2 **10
        ))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


def calculate_frequencies(file_contents):
    # A list of punctuation and other uninteresting words
    # that will be omitted when creating the word cloud
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ['the', 'a', 'to', 'if', 'is', 'it', 'of', 'and', 'or', 'an', 'as', 'i', 'me', 'my', \
        'we','our', 'ours', 'you', 'your', 'yours', 'he', 'she', 'him', 'his', 'her', 'hers', 'its', 'they', 'them', \
        'their', 'what', 'which', 'who', 'whom', 'this', 'that', 'am', 'are', 'was', 'were', 'be', 'been', 'being', \
        'have', 'has', 'had', 'do', 'does', 'did', 'but', 'at', 'by', 'with', 'from', 'here', 'whem', 'where', 'how', \
        'all', 'any', 'both', 'each', 'few', 'more', 'some', 'such', 'no', 'nor', 'too', 'very', 'can', 'will', 'just']

    # =========== Actual code starts here ===========

    frequencies = {}
    taken = []
    for letter in punctuations:
        file_contents = file_contents.replace(letter, '')
    for word in uninteresting_words:
        w = ' ' + word + ' '
        file_contents = file_contents.replace(w, ' ')
    for word in file_contents.split():
        if word.lower() not in taken:
            taken.append(word.lower())
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

# Display wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
