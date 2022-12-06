#! /usr/bin/env python3

import rospy                                            # Importamos las librerías necesarias
from std_msgs.msg import Int32                          

rospy.init_node('topic_publisher')                      # Nombre del nodo
pub = rospy.Publisher('/counter', Int32, queue_size=1)  # /counter: tópico. Int32: tipo de mensaje. queue_size: cola de mensaje
rate = rospy.Rate(2)                                    # Veces por segundo que se ejecuta el nodo
count = Int32()                                         # Creamos el contador
count.data = 0                                          # Iniciamos el contador a 0

while not rospy.is_shutdown():                          # Mientras no hagamos CTRL-C
    pub.publish(count)                                  # Publicamos el valor de count
    count.data += 1                                     # Modificamos el valor del contador
    rate.sleep()                                        # Volvemos a ejecutar