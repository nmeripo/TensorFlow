# Import the tensorflow module and call it tf
import tensorflow as tf 

# Create a constant value called x, and give it the numerical value 74
x = tf.constant(74, name = 'x')

# Create a Variable called y, and define it as being the equation x + 3
y = tf.Variable(x + 3, name = 'y')

# Initialize the variables with global_variables_initializer since initialize_all_variables is deprecated
model = tf.global_variables_initializer()

# Create a session for computing the values
with tf.Session() as session:
	# Run the model
	session.run(model)
	# Run just the variable y and print out its current value
	print session.run(y)

