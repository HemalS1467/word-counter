from flask import Flask, request

app = Flask(__name__)

class WordCounter:
    """
    Class WordCounter 
    """
    def __init__(self, string):
        self.string = string
        self.word_counts = {}
       
    def count_repetition(self):
        """
        Method to count the repetition of each word (alphanumeric).
        """
        
        for word in self.string.split():
            if word.isdigit():
                word = int(word)
            elif not  word.isalnum():
                continue
            self.word_counts[word] = self.word_counts.setdefault(word,0)+1
            
        sorted_words = sorted(self.word_counts, key=lambda x: (not isinstance(x,int),x))
        return [(word, self.word_counts[word]) for word in sorted_words]

    def count_total_words(self):
        """
        Method to count the total number of words
        Args:
            No Args
        """
        
        return sum(list(self.word_counts.values()))
    
    def count_total_characters(self,with_spaces=True):
        """
        Method to count the total number of characters, a) with spaces, b) without spaces
        Args:
            with_spaces : Bool | (True,False)

        """
        if with_spaces:
            return len(self.string)
        return len(self.string.replace(" ", ""))
   

@app.route('/word_counter', methods=['POST'])
def word_counter():
    """
    urls: localhost:5000/word_counter
    method:POST
    form-data:
        string="abc sdjw 1 2"
    
    """
    word_counter = WordCounter(request.form['string'])
    return {
        'repetition': word_counter.count_repetition(),
        'total_words': word_counter.count_total_words(),
        'total_characters_with_spaces': word_counter.count_total_characters(),
        'total_characters_without_spaces': word_counter.count_total_characters(with_spaces=False)

    }

if __name__ == '__main__':
    app.run(debug=True)
