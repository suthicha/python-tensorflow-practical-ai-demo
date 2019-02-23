import tensorflow as tf

# create variable a with scalar value.
a = tf.Variable(2, name="scalar")

# create variable b as a vector.
b = tf.Variable([2, 3], name="vector")

# create variable W as 784 x 10 tensor, filled with zeros.
W = tf.Variable(tf.truncated_normal([700, 10]))

# init_ab = tf.variables_initializer([a, b], name="init_ab")

with tf.Session() as session:
    session.run(W.initializer)
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(W.eval()))

writer.close()

