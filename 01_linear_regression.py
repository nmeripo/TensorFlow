import tensorflow as tf
import numpy as np

train_X = np.linspace(-1, 1, 101)

# create a y value which is approximately linear but with some random no.
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * .33

# create symbolic variables
X = tf.placeholder("float")
Y = tf.placeholder("float")


# linear regression is just X*w so this model line is pretty simple
def model(X, w):
    return tf.multiply(X, w)

# create a shared variable for the weight matrix
w = tf.Variable(0.0, name="weights")
model_Y = model(X, w)

# use square error for cost function
cost = tf.square(Y - model_Y)

# construct an optimizer to minimize cost and fit line to the data
train_op = tf.train.GradientDescentOptimizer(.01).minimize(cost)

# Launch the graph in a session
with tf.Session() as session:
    # you need to initialize variables (in this case just variable W)
    tf.global_variables_initializer().run()
    for i in range(100):
        for (x,y) in zip(train_X, train_Y):
            session.run(train_op, feed_dict={X: x, Y: y})

    print  session.run(w) # It should be something around 2
