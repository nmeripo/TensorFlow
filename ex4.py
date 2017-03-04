import tensorflow as tf 
import numpy as np


average = tf.Variable(0, name = 'y')

model = tf.global_variables_initializer()


with tf.Session() as session:
	session.run(model)
	for i in range(5):
		x = np.random.randint(1000)
		average = (average + x) / 2
		print session.run(average)
