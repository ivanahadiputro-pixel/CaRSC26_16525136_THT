#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class WatchSubscriber : public rclcpp::Node
{
public:
WatchSubscriber() : Node("Watch")
{
subscription_ = this->create_subscription<std_msgs::msg::String>("time", 10, std::bind(&WatchSubscriber::time_callback, this, std::placeholders::_1));

}
private:
void time_callback(const std_msgs::msg::String::SharedPtr msg)
{
RCLCPP_INFO(this->get_logger(), "Current time : %s", msg->data.c_str());

}

rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

};

int main(int argc, char *argv[])
{
rclcpp::init(argc, argv);
rclcpp::spin(std::make_shared<WatchSubscriber>());
rclcpp::shutdown();
return 0;

}
