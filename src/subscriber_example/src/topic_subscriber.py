#! /usr/bin/env python3

import rospy

from std_msgs.msg import Int32                      # Importamos el tipo de mensaje que recibirá

rospy.init_node('topic_subscriber')                 # Nombramos el nodo

def printCount(data):                               # Función que imprime el valor leído por consola
    print(data)

rospy.Subscriber('/counter', Int32, printCount)     # Lectura del tópico y llamada a función anterior.
rospy.spin()                                        # Vuelve a ejecutar