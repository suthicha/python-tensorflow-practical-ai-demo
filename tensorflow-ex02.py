import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a,b)

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(x))

# close the writer when we have done.
writer.close()

