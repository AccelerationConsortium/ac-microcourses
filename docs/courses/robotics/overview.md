

<!--- WARNING: THIS IS AN AUTO-GENERATED FILE. DO NOT EDIT DIRECTLY. Instead,
edit in docs/course-data.yaml and run the `scripts/generate_overviews.py` file
or modify src/ac_microcourses/overview.md.jinja. --->

# 🦾 Robotics: Course Overview



Embark on a journey into the world of robotics and automation for self-driving laboratories. This asynchronous, remote course equips you with the skills to control peristaltic pumps, linear actuators, automated liquid handlers, and solid dispensers using a microcontroller, a motor driver, and a workflow orchestration package. You'll also learn to control mobile cobots and perform spatial referencing and ID recognition via computer vision. The course will conclude with a solid sample transfer workflow using a multi-axis robot. Remotely accessible resources will be provided as necessary.


```{margin}
Self-driving lab robotic platforms. 1. ADA at the University of British Columbia (C. Berlinguette, J. Hein, A. Aspuru-Guzik); 2. Artificial Chemist (M. Abolhasani, NC State University); 3. Robotically reconfigurable flow chemistry platform (C. Coley, MIT); 4. Chemputer (L. Cronin, University of Glasgow); 5. Mobile robot chemist (A. Cooper, University of Liverpool). Source: [https://acceleration.utoronto.ca/maps](https://acceleration.utoronto.ca/maps)
```


<video width='100%' controls autoplay muted><source src='./../../_static/ac-website/robot-loop.mp4' type='video/mp4'>Your browser does not support the video tag.</video>


## 🔑 Prerequisites



The **recommended prerequisite** for this course is Introduction to AI for Discovery using Self-driving Labs


## 🎯 Learning Outcomes


- Design and execute software to manage a peristaltic pump's operations using a microcontroller and motor driver, demonstrating application and integration skills

- Construct the "Digital Pipette" and develop software to manipulate the linear actuator, showcasing capabilities in hardware assembly and software programming

- Operate an automated liquid handler, such as Science Jubilee or Opentrons, to accurately transfer liquid between vials, demonstrating proficiency in laboratory automation techniques

- Exhibit the ability to control a mobile collaborative robot (cobot) using the ROS framework, reflecting advanced understanding and operational skills in robotics

- Showcase the use of OpenCV and AprilTags for spatial referencing and ID lookup, illustrating advanced skills in computer vision and object identification

- Configure and utilize ROS, AprilTags, and a multi-axis robot to execute solid sample transfers, demonstrating integrated skills in robotics programming and operation



## 🛠️ Competencies/Skills


- Motor drivers

- Serial communication

- Automated liquid handlers

- Robotic control

- Robotic simulation

- Computer vision

- Automated solid handlers



## 🧩 Modules

Each module is intended to take approximately 3-4 hours, assuming that the recommended prerequisites have been met.

```{list-table}
:header-rows: 1

* - Module Name
  - Topics
  - Learning Outcomes

* - 3.0 Orientation
  - * Git
    * GitHub
    * Version control
    * GitHub Classroom
    * Codespaces
  - * Describe the purpose of Git and GitHub
    * Create a GitHub account and a repository
    * Commit, push, and pull changes
    * Run a unit test and fix a simple Python function
    * Define continuous integration

* - 3.1 Pumps and Pipettes
  - * Workflow orchestration
    * Microcontrollers
    * Peristaltic pumps
    * Linear actuators
    * Motor drivers
  - * Implement software to control a peristaltic pump via a microcontroller and a motor driver
    * Build the "Digital Pipette" and implement software to control the linear actuator

* - 3.2 Serial communication
  - * Mass balance
    * Serial communication
    * Reading data
  - * Design and execute software to read data from a mass balance using serial communication

* - 3.3 Liquid Handlers
  - * Workflow orchestration
    * Jubilee
    * Opentrons
  - * Perform liquid transfer between vials with an automated liquid handler (Science Jubilee and OT-2)

* - 3.4 Mobile robotics
  - * ROS
    * Isaac Sim
    * Asynchronous task execution
    * Prefect
  - * Demonstrate control of a mobile cobot using frameworks such as the Robot Operating System (ROS) and Isaac Sim
    * Use a workflow orchestration package to manage asynchronous tasks
    * Define asynchrony in the context of hardware control for automonous laboratories

* - 3.5 Computer vision
  - * OpenCV
    * AprilTags
  - * Demonstrate spatial referencing and ID lookup by using OpenCV and AprilTags
    * Use a motorized microscope and OpenCV to search for regions of interest in a sample

* - 3.6 Solid sample transfer
  - * Workflow orchestration
    * ROS
    * AprilTags
    * Multi-axis robotics
  - * Use ROS, AprilTags, a multi-axis robot, and a workflow orchestration platform to perform solid sample transfer

```

## ⚖️ Course Assessments and Grading Schema

<p>Each student is required to complete various quizzes and GitHub Classroom assignments. The course is structured into an orientation module followed by several modules. The course is graded on a pass/fail basis with 70% as the threshold for passing. Here is the breakdown of the points for each part of the course:</p><ul><li>🧭 Orientation Module: Worth 15 points.</li><li>📚 Modules 1-6: Each includes:<ul><li>🧭 A guided notebook tutorial (ungraded)</li><li>📓 A knowledge check (graded, 5 points)</li><li>🛠️ A GitHub Classroom assignment (graded, 10 points*)</li></ul></li></ul><p>*The final module's GitHub Classroom assignment is worth 30 points.</p><p>Note that partial points are available on certain assignments.</p>


## 👤 Course developer(s)


- Sterling Baird, PhD Materials Science and Engineering (Acceleration Consortium)
