import rclpy
from rclpy.node import Node 
from std_msgs.msg import String
import Rpi.GPIO as GPIO 
 
class Warning_Publisher(Node):

	def __init__(self):
		super().__init__('warning_publisher')

		# Setting up the GPIO
		self.channel = 4
		GPIO.setwarning(False)	   #Ignore warnings
		GPIO.setmode(GPIO.BOARD)   #Use physical pin numbering
		GPIO.add_event_dectect(self.channel, GPIO.RAISING)
		
		# Create publisher 
		self.publisher_ = self.create_publisher(String,'\String_topic',10)
		tm_period = 1
		self.time = self.create.timer(tm_period, self.callback)
 
	def callback(self):
		msg = String()
		if GPIO.event_detected(self.channel):
			msg.data = 'Warining Button pressed'
			self.get_logger.info("Publishing Warning")
			self.publisher.publish(msg)

def main(args=None):
	rclpy.init(args=args)
	warning_pub = WarningPublisher()
	rclpy.spin(warning_pub)
	rclpy.shutdown()


if __name__ == '__main__':
    main()
