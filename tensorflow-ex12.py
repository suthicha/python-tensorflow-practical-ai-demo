import tensorflow as tf
# import numpy as np

# for m in np.linspace(0, 10, 4):
#    print(m)

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    for x in tf.linspace(0.0, 10.0, 4):
        print(session.run(x))

# close the writer when we have done.
writer.close()

