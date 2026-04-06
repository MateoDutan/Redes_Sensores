# Usamos la imagen oficial
FROM osrf/ros:jazzy-desktop

# Actualizamos e instalamos las extensiones de colcon y matplotlib (para graficar)
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3-colcon-common-extensions nano python3-matplotlib && \
    rm -rf /var/lib/apt/lists/*

# Creamos el workspace
RUN mkdir -p /root/ros2_ws/src
WORKDIR /root/ros2_ws/src

# Creamos el paquete sensor_program automáticamente
RUN bash -c "source /opt/ros/jazzy/setup.bash && ros2 pkg create --build-type ament_python sensor_program --license MIT"

# Nos ubicamos en la raíz del workspace
WORKDIR /root/ros2_ws

# Utilizamos el entrypoint oficial de ROS 2 que carga las variables de entorno
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
