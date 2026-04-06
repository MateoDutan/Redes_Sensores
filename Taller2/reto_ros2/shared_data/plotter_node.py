import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import matplotlib.pyplot as plt
import re

class PlotterNode(Node):
    def __init__(self):
        super().__init__('plotter_node')
        self.subscription = self.create_subscription(
            String,
            'sensor_data',
            self.listener_callback,
            10)
        
        self.temperatures = []
        self.times = []
        self.time_counter = 0
        
        # Temporizador para graficar cada 5 segundos
        self.timer = self.create_timer(5.0, self.plot_data)

    def listener_callback(self, msg):
        # Extraemos solo el número del mensaje (ej: "Temperatura: 25 C" -> 25)
        match = re.search(r'\d+', msg.data)
        if match:
            temp = int(match.group())
            self.temperatures.append(temp)
            self.times.append(self.time_counter)
            self.time_counter += 1 # Asumimos que llega 1 por segundo

    def plot_data(self):
        if not self.temperatures:
            return
            
        plt.figure()
        plt.plot(self.times, self.temperatures, marker='o', color='b')
        plt.title('Temperatura a lo largo del tiempo')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Temperatura (°C)')
        plt.grid(True)
        
        # Guardamos la gráfica en la carpeta compartida (Volumen)
        # Todo lo que se guarde aquí, aparecerá mágicamente en tu computadora real
        plt.savefig('/root/ros2_ws/data/sensor_plot.png')
        plt.close()
        self.get_logger().info('Gráfico actualizado y guardado en /root/ros2_ws/data/sensor_plot.png')

def main(args=None):
    rclpy.init(args=args)
    node = PlotterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
