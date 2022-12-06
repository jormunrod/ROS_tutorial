#! /usr/bin/env python3

import rospy                                # Importamos las librerías que necesitamos.

rospy.init_node('ArusNode')                 # Nombre del nodo.

rate = rospy.Rate(2)                        # Veces por segundo que se ejecutará el bucle
while not rospy.is_shutdown():              # El nodo se ejecutará hasta que hagamos CTRL-C
    print("Pronto conduciremos sin manos")  # La acción que hará el nodo.
    rate.sleep()                            # Cuando llegue aquí, vuelve a ejecutarse