##Python packages
import spacy
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
# Import Heapq for Finding the Top N Sentences
from heapq import nlargest

def spacy_summarizer(raw_data):
        r_text= raw_data
        doc= nlp(r_text)
        #list of stopwords
        stopwords= list(STOP_WORDS)
        word_freq= dict()        #dictionary to store words and their frequency
        for word in doc:
                if word.text not in stopwords:
                        if word.text not in word_freq.keys():
                                word_freq[word.text]=1;
                        else:
                                word_freq[word.text]+=1

        #max frequency of word in the document
        max_freq= max(word_freq.values())
        for word in word_freq.keys():  
                word_freq[word] = (word_freq[word]/max_freq)
        
        # Sentence Tokens
        s_list = [s for s in doc.sents]

        # Sentence Scores
        s_scores=dict()
        for s in s_list:  
                for w in s:
                        if w.text.lower() in word_freq.keys():
                                if len(s.text.split(' ')) < 30:
                                        if s not in s_scores.keys():
                                                s_scores[s] = word_freq[w.text.lower()]
                                        else:
                                                s_scores[s] += word_freq[w.text.lower()]


        summarized_Text = nlargest(7, s_scores, key=s_scores.get)
        final_text = [w.text for w in summarized_Text]
        summary = ' '.join(final_text)
        print(summary)
        return summary
