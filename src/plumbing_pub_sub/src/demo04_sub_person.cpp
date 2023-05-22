#include "ros/ros.h"
#include "plumbing_pub_sub/person.h"

void domsg(const plumbing_pub_sub::person::ConstPtr& person)
{
    ROS_INFO("订阅:%s,%d,%.2f",person->name.c_str(),person->age,person->height);
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ROS_INFO("订阅方");

    ros::init(argc,argv,"jiazhang");

    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("liaotian",10,domsg);

    ros::spin();

    return 0;
}
