import tensorflow as tf

a = tf.fill([2,3], 8)

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(a))

# close the writer when we have done.
writer.close()

