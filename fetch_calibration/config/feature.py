import rosbag

with rosbag.Bag('output_led.bag', 'w') as outbag:
    for topic, msg, t in rosbag.Bag('output_gripper.bag').read_messages():
              # This also replaces tf timestamps under the assumption 
              # that all transforms in the message share the same timestamp
              #print 'convert a message'
              msg.features.remove("gripper_depth_finder")
              msg.features.append("led_finder")
              outbag.write(topic, msg, t)

