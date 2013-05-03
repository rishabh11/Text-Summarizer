""" This class operates on the neural net saved in file auto_sum.net.
Basically we have taken 5 input layered neurons, 4 hidden layer neuron and 1 output layer neuron.
The input layer neuron correspond to the 5 features of a summary-
sentence location, first sentence, sentence length, number of thematic words, number of title words.
Weights are updated as per the new summaries given.
The more the use of a feature in a summary the weights of input layer are increased followed by the increae in weights of hidden layer the output.
Thresholds for each layer have been set as according to observation.
"""

class nn:	
	num_trained=0
	matih=[[],[],[],[],[]]		#weight matrix for input layer
	matho=[]			#weight matrix for hidden layer
	inp=[0]*5			#input being 1 or not
	hid=[0]*4			#hidden being 1 or not
	out=0				#output being 1 or not
	""" thresholds for all layers-"""	
	thresh_inp=0.4
	thresh_hid=0.5
	thresh_out=0.3

	def load_net(self):
		""" loads net from the file into matrix and other values"""
		net_file=open("auto_sum.net","r")
		temp=net_file.readlines()
		ind=0	
		for line in temp:
			if(line=="\n"): break
			self.matih[ind]=line.split()	#loading weight matrix for input layer
			ind+=1
		self.matho=temp[-3].split()		#loading weight matrix for hidden layer
		self.out=float(temp[-2])		# weight matrix for output layer
		self.num_trained=float(temp[-1])	#number of times already trained
		for i in range(5):
			for j in range(4):
				self.matih[i][j]=float(self.matih[i][j])
		for i in range(4): self.matho[i]=float(self.matho[i])
		net_file.close()
			
	def update_weight(self,new_inp_weights):
		""" Given a input set of weights, the function updates the matrix"""
		#updating input matrix
		for i in range(5):
			if(new_inp_weights[i]!=0):
				self.inp[i]=1
				for j in range(4):
					self.matih[i][j]=(self.matih[i][j]*self.num_trained+new_inp_weights[i])/(self.num_trained+1)	

		#updating hidden matrix		
		for i in range(4):
			sum_inp_weights=0
			count=0
			for j in range(5):
				if self.matih[j][i]*self.inp[j] > self.thresh_inp :
					sum_inp_weights+=self.matih[j][i]
					count+=1
			if count==0 : count=1
			self.matho[i]=(self.matho[i]*self.num_trained+sum_inp_weights/count)/(self.num_trained+1)
			self.hid[i]=1

		#updating output		
		sum_hid_weights=0
		count =0
		for i in range(4):
			if self.matho[i]*self.hid[i] > self.thresh_hid :
				sum_hid_weights+=self.matho[i]
				count+=1
		if count==0 : count=1
		self.out = (self.out * self.num_trained+sum_hid_weights/count)	/(self.num_trained+1)
		
		self.num_trained+=1	#increases num of times trained

	def save_net(self):
		""" Saves the new updated network in auto_sum.net after training."""
		net_file=open("auto_sum.net","w")
		for i in self.matih:
			for j in i:
				net_file.write(str(j)+" ")
			net_file.write("\n")
		net_file.write("\n")
		for i in self.matho:
			net_file.write(str(i)+" ")
		net_file.write("\n"+str(self.out)+"\n"+str(self.num_trained))
		net_file.close()
			
	def check_imp_feature(self):
		"""Returns 1 if and only if output weight greater then its threshold"""		
		if self.out>self.thresh_out : return 1
		return 0

