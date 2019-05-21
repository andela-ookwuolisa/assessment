### Web Application Performance and Scalability
An application performance is measured in terms of its responsiveness, throughput, and resource utilization under a given workload. Note that an application performance will vary based on its workload.

Scalabilty refers to how an application is able to respond to additional load while maintaining the same level of performance by adding additional server resources such as CPU, memory, disk.

#### Vertical and horizontal scalling

Vertical scaling is when we scale forthe short term. This is because it is cheap and easy to implement. Vertical scaling means that you scale by adding more power (CPU, RAM) to an existing machine. In a scenario where by you notice that the application is probably slow you can just increase the memory (RAM) capacity of the system. Usually this scaling is limited and has only one server. For instance increasing the memory capacity of my machine for 8gb to 16gb to improve the system performance.

Horizontal scaling means that you scale by adding more machines into your pool of resources. Horizontal scaling is more suitable for long term, this is because it is more expensive to implement and in some cases you might want to change the architecture and configuration of the system. This basically involves connecting multiple entities/ servers so that they work as a single logical unit.

##### Autoscaling
Autoscaling enables an increase (scaled out) or decrease (scaled in) the number of servers/machines based on the load on the system. Most cloud computing services like AWS, Microsoft Azure etc support autoscaling. 

#### Benefits of measuring performance and scalability
- Assess production readiness.
- Identify areas that needs improving
- Assess adequacy of software.
- Improve efficiency of performance tuning by identifying bottle necks.
- Accurate data on infrastructure requirements and costs to meet application performance and scalability goals.
- Assurance that current infrastructure will meet anticipated user demand.

#### What Metrics To Measure
- Total Availability: Total availability reveals the ability of your end users to access to your service or mobile app through the day and from day to day over a longer period.
- Time To First Byte (TTFB). This measures the responsiveness of your mobile app. It indicates how fast your app is able to launch and get the first responses from the back end servers.
- Reaction Time. It’s the measurement that reflects the speed at which your mobile application reacts to user inputs. For example, ‘How fast your application starts showing search results’, ‘How fast the business transactions are completed’, etc.
- Time To Load. This is a metric that implies the time elapse between the moment users launch your app and the moment users can start interacting with your app. It tells how fast the application becomes responsive to user queries.

#### What to measure (Load Characteristics)
- User Load: how many users are being simulated in accessing the system at a given time.
- Request per second.
- Errors per second.

#### What to measure (Resource Utilization per server)
- CPU
- Memory
- Disk/Network

#### Kinds of test
- Performance Test: determine or validate speed of the application.
- Load Test: Determines how an application's performance varies as load increases.
- Stress Test: its a kind of load test, that determines application behaviour when pushed beyond normal or peak load conditions.

