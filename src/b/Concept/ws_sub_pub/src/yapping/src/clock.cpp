#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class ClockPublisher : public rclcpp::Node
{
public:
ClockPublisher() : Node("clock")
{

publisher_ = this->create_publisher<std_msgs::msg::String>("time", 10);

timer_ = this->create_wall_timer(1s, std::bind(&ClockPublisher::publish_time, this));
}
private:
void publish_time()
{
auto now = std::chrono::system_clock::now();
std::time_t now_time =std::chrono::system_clock::to_time_t(now);


std::tm *utc = std::localtime(&now_time);

std::stringstream ss;
ss << std::put_time(utc, "%Y-%m-%dT%H:%M%S");

std_msgs::msg::String msg;
msg.data = ss.str();

publisher_->publish(msg);

RCLCPP_INFO(this->get_logger(), "Published time: %s", msg.data.c_str());

}

rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
rclcpp::TimerBase::SharedPtr timer_;

};

int main(int argc, char *argv[])
{
rclcpp::init(argc, argv);
rclcpp::spin(std::make_shared<ClockPublisher>());
rclcpp::shutdown();
return 0;

}




