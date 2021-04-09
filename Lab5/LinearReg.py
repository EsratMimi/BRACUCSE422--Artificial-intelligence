# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import matplotlib.pyplot as plt 

def estimate_co(x, y): 
	
	n = np.size(x) 

	
	m_x, m_y = np.mean(x), np.mean(y) 


	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 

	
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x # y-b1*x 

	return(b_0, b_1) 

def plot_line(x, y, b): 
    
	plt.scatter(x, y, color = "m", 
			marker = "o") 


	y_pred = b[0] + b[1]*x # b1+b2*x+...+bn*bn


	plt.plot(x, y_pred, color = "g") 

	plt.xlabel('x') 
	plt.ylabel('y') 


	plt.show() 

def main(): 
    
	x = np.array([1,4,5,7,8,9,12]) 
	y = np.array([1,10,12,14,15,12,20]) 


	b = estimate_co(x, y) 
	print("Estimated coefficients:\n{}\n{}".format(b[0], b[1])) 


	plot_line(x, y, b) 

if __name__ == "__main__": 
	main() 
