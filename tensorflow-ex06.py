import tensorflow as tf

input_tensor = [[0,1],[2,3],[4,5]]
a = tf.zeros_like(input_tensor)

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(a))

# close the writer when we have done.
writer.close()

