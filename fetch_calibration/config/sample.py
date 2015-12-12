import subprocess, yaml
import random
import rosbag

## Config
bag_file_name    = 'calibration_poses.bag'
sampled_bag_name = 'calibration_poses_sampled_50.bag'
topic_name       = 'calibration_joint_states'
num_to_sample    = 25

info_dict        = yaml.load(subprocess.Popen(['rosbag', 'info', '--yaml', bag_file_name], stdout=subprocess.PIPE).communicate()[0])
topic_dict       =  info_dict['topics']
num_messages     = 0
for x in topic_dict:
    if x['topic'] == topic_name:
        num_messages = x['messages']

indices = []
num     = 0
for i in range(0,num_to_sample):
    while num in indices or num == 0:
        num = int(random.uniform(1,num_messages))
    indices.append(num)

indices = sorted(indices)
print indices

bag         = rosbag.Bag(bag_file_name)
bag_sampled = rosbag.Bag(sampled_bag_name, 'w')
index   = 1
for topic, msg, t in bag.read_messages(topics=[topic_name]):
    if index in indices:
        bag_sampled.write(topic, msg, t)
    index +=1
bag.close()
bag_sampled.close()
