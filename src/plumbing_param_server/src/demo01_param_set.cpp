#include "ros/ros.h"

int main(int argc, char *argv[])
{
    ros::init(argc,argv,"set_c");

    ros::NodeHandle nh;

    nh.setParam("type","xiaohuang");
    nh.setParam("rasius",0.5);

    ros::param::set("type_param","xiaobai");
    
    return 0;
}