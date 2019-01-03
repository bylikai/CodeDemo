import tensorflow as tf 

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session() 

hello = tf.constant("Tensorflow world!")
print( sess.run(hello) ) 

a = tf.constant( 72.5 )
b = tf.constant( 33.6 )
print( sess.run( a+b ) )

sess.close()

