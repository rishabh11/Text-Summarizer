import text_proc
import nn

class summarize:
	"""import the other two classes. Uses them to train and generate summary."""
	tp=text_proc.text_proc()

	def train(self,title,para,summary):	#training	
		weights=self.tp.generate_weights(para,title,summary)
		net=nn.nn()		
		net.load_net()
		net.update_weight(weights)
		net.save_net()
	
	def generate_summary(self,title,para):		#generates summary by paaing every sentence through the net and checking if output=1 or not
		summary=""
		para1=para.split(".")
		for lines in para1:
			weights=self.tp.generate_weights(para,title,lines)	
			net=nn.nn()			
			net.load_net()
			net.update_weight(weights)
			if(net.check_imp_feature()==1): 	#checks whether the given sentence imp for including in summary or not
				summary+=lines
				if summary[-1]!='.' : summary+='.'
		return summary
	
