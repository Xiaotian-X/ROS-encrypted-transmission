#include "ros/ros.h"
#include "plumbing_pub_sub/person.h"

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ROS_INFO("发布方");

    ros::init(argc,argv,"banzhuren");

    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<plumbing_pub_sub::person>("liaotian",10);

    plumbing_pub_sub::person Person;
    Person.name = "张三";
    Person.age = 1;
    Person.height = 1.73;

    ros::Rate rate(1);

    while(ros::ok())
    {
        Person.age += 1;

        pub.publish(Person);
        ROS_INFO("发布的消息：%s,%d,%.2f",Person.name.c_str(),Person.age,Person.height);

        rate.sleep();

        ros::spinOnce();
    }

    return 0;
}
