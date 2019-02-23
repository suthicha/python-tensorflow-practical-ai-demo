import tensorflow as tf

a = tf.linspace(10.0, 13.0, 4, name="linspace")

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(a))

# close the writer when we have done.
writer.close()

