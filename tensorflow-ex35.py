import tensorflow as tf

# create Operations, Tensors, etc(using the default graph)
a = tf.add(2,5)
b = tf.multiply(a, 3)

# start up a 'session' using the default graph.
session = tf.Session()

# define a dictionary that says to replace the value of 'a' with 15
replace_dict = {a: 15}

print(session.run(b, feed_dict=replace_dict))

# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#
#     for a_value in [[1, 2, 3], [4, 5, 6]]:
#         print(session.run(c, {a:a_value}))
#
# writer.close()

