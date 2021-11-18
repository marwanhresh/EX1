SMART ELEVATOR

links:

1.https://www.youtube.com/watch?v=JXqVvmBOyyQ&list=PLdpEqO8FXeP5wB1fgD-DMAezJ6gHnGdkh&index=19&t=73s

2.https://www.youtube.com/watch?v=siqiJAJWUVg&list=PLdpEqO8FXeP5wB1fgD-DMAezJ6gHnGdkh&index=18
3.https://medium.com/geekculture/system-design-elevator-system-design-interview-question-6e8d03ce1b44

I. The Elevator ProblemIn a multi-storied building people use the elevator to travel between floors.
The problem is to schedule the elevator in “the best possible way”.
The problem in detail: There are ‘F’ floors in a building.
There is oneelevator that we are concerned with.
There are elevator-service-requests coming from people on each floor according to some distribution.
The request comes at a particular time.
The request is to go from one floor (source) to another (destination).
The goal is to schedule the elevator in the best possible way.We need to define what we mean by “the best possible way”.
II. Research question and motivation We need to find out which on-line algorithm gives a “good” solution.We need to define the goodness of the offline algorithm.
“Which on-line algorithm best approximates the optimal off-line algorithm (if one exists) for the elevator scheduling problem?”For this we need to define What we mean by the optimal solution.
The performance metrics for the on-line algorithms.
We need to qualify the term “optimal” based on some criteria, for example in this case of the elevator scheduling problem the criteria could be one/more of the following:

1.The distance covered by the elevator in unit time should be the minimum.
2.The number of passengers served per unit time should be the maximum.
3.The average response time per request on any floor should be the minimum.
4.The average waiting time per person on any floor should be the minimum.We choose the 3rdoption

How is the elevator assigned to the user?

*When a user presses their desired floor on the keyboard, it goes through the following steps:

He checks if there is an elevator on that floor, if so, she assigns the elevator.
If not, he checks if the user wants to move to the top floor or the bottom floor from his current floor.
He then assigns the elevator that ascends and approaches the same floor.
The material limitation in the algorithm is that an elevator cheat can be a maximum of 4 stations. Whether the elevator has reached its maximum stops or not.
*What is the system and how does it work?

Each elevator maintains a queue (data structure). The number of elements in the queue is the maximum number of stops that can be in the elevator.
The first element in line is its current floor. The following elements are its objectives in order.
The lift goes up when the difference between the current element and the next element is positive and vice versa

Waiting Time on Calling Elevator By Utilizing Context Aware Platform in Smart Elevator

Elevator system faces a serious challenge of reducing waiting time for passengers because of the computation limitation of the stand-alone elevator system. In this article, we present our proposal–PrecaElevator, a novel elevator system in smart building that enables passengers to reduce their waiting time through pre-registering elevator calls. After upgraded a traditional elevator to Internet of Things (IoT)-enabled and transferred the real-time computational capability to the agent server, the elevator was upgraded as a smart object computing on context awareness in both elevator and passengers. By leveraging BLE-based localization of the passenger, PrecaElevator enables the passenger to pre-register elevator call if his/her location was detected within the callable range for elevator control. We have experimented the proposed system in the real smart building environment. The simulations based on the calculated waiting time from elevator historical records showed the effectiveness of waiting time reduction.

