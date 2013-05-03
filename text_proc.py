""" Does the basic text processing. 
Finds the new weights by looking for any of the five features in a given sentence of a paragraph. 
Library used is nltk for a corpora of stopwords and a stemmer
The nltk library can be downloaded from- http://www.nltk.org/download"""

from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer

class text_proc:
	def pre_proc(self,text):
		""" This functios for a given paragraph, reduces it to list of words and sentences. The removes stop words followed by stemming using lancaster stemmer."""
		final_text=[]
		lancas=LancasterStemmer()
		text=text.split("\n")
		for line in text:
			sent=line.split(".")
			for i in sent:
				temp_sent=i.split()
				final_sent=[]
				for word in temp_sent:
					if word not in stopwords.words():	#checks if not a stop word
						final_sent.append(lancas.stem(word))	#stems the word
				final_text.append(final_sent)					
		if len(final_text)==1: final_text=final_text[0]
		return final_text

	def sent_loc(self,para,sent):
		""" Check wether a given sentence is in top quarter of para""" 
		if sent in para[:len(para)/4]: return 1
		return 0

	def first_sent(self,para,sent):
		""" Check wether a given sentence is first sentence of para""" 
		if(sent==para[0]): return 1
		return 0

	def sent_len(self,para,sent):
		""" Check wether a given sentence is of length greater than the average lengths of all sentences in para""" 
		avg_len=0
		for i in para:
			avg_len+=len(i)
		avg_len/=len(para)
		if(len(sent)>=avg_len): return 1
		return 0

	def thematic_words(self,para,sent):
		""" Check wether a given sentence has any top 5 frequent para""" 
		most_freq_words=self.frequency(para)[:5]
		count=0
		for words in sent:
			if words in most_freq_words: count+=1
		if count>=len(sent)/2 : return 1
		return 0

	def frequency(self, para):
		"""frequency of all words in a para- this function used in thematic_words"""
		dict={}
		for i in para:
			for j in i:
				if j not in dict.keys():
					dict[j]=0
		for i in para:
			for j in i:
				dict[j]+=1
		return sorted(dict,key=dict.get,reverse=True)

	def title_words(self,sent,title):
		""" checks if there is a title word in the sentence"""
		lancas=LancasterStemmer()
		title=lancas.stem(title)
		count=0
		for words in sent:
			if words==title : return 1
		return 0

	def generate_weights(self,para,title,summary):
		"""returns a list of weights as according to the features existing in all the sentences
		of the given summary"""
		para=self.pre_proc(para)
		summary=self.pre_proc(summary)
		ls=[0.0]*5
		for sent in summary:
			if self.sent_loc(para,sent): ls[0]+=1
			if self.first_sent(para,sent): ls[1]+=1
			if self.sent_len(para,sent): ls[2]+=1
			if self.thematic_words(para,sent): ls[3]+=1
			if self.title_words(sent,title): ls[4]+=1
		for i in range(len(ls)):
			if len(summary)!=0: ls[i]/=len(summary)
		return ls
	
