import tensorflow as tf

# create a placeholder of type float 32bit, shape is a vector of 3 elements
a = tf.placeholder(tf.float32, shape=[3])

# create a constant of type float 32bit, shape is a vector of 3 elements
b = tf.constant([5, 5, 5], tf.float32)

# use the placeholder as you would a constant or a variable.
c = a + b

# If try to fetch c variable, It's make to error.

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(c, {a: [1, 2, 3]}))

writer.close()

