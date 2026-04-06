import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ReaderNode(Node):
    def __init__(self):
        super().__init__('reader_node')
        self.subscription = self.create_subscription(
            String,
            'sensor_data',
            self.listener_callback,
            10)
        self.subscription  # evitar que la variable sea eliminada por el recolector

    def listener_callback(self, msg):
        self.get_logger().info(f'He recibido: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = ReaderNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
