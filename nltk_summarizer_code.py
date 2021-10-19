import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq  

def nltk_summarizer(initial_text):
    r_text=initial_text
    stopWords = set(stopwords.words("english"))
    word_freq = dict() 
    for word in nltk.word_tokenize(r_text):  
	    if word not in stopWords:
	        if word not in word_freq.keys():
	            word_freq[word] = 1
	        else:
	            word_freq[word] += 1

	
    
    max_frequncy = max(word_freq.values())

	
    
    for word in word_freq.keys():  
	    word_freq[word] = (word_freq[word]/max_frequncy)

	
    
    s_list = nltk.sent_tokenize(r_text)
    s_scores = dict()  
    for sent in s_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_freq.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in s_scores.keys():
	                    s_scores[sent] = word_freq[word]
	                else:
	                    s_scores[sent] += word_freq[word]

    
    
    summary_text = heapq.nlargest(7, s_scores, key=s_scores.get)
    final_text = ' '.join(summary_text)  
    #print(final_text)
    return final_text







'''nltk_summarizer("The first Harmandir Sahib was built in 1604 by Arjan, the fifth Sikh Guru, who symbolically had it placed on a lower level so that even the humblest had to step down to enter it. He also included entrances on all four sides, signifying that it was open to worshippers of all castes and creeds. The foundation stone was laid by Mian Mīr, a Muslim divine of Lahore (now in Pakistan). The temple was destroyed several times by Afghan invaders and was finally rebuilt in marble and copper overlaid with gold foil during the reign (1801–39) of Maharaja Ranjit Singh. The structure thus became known as the Golden Temple.")'''



