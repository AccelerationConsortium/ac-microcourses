# Microcourses

Here, we provide details for the five core microcourses, including title, description, learning outcomes, skills, and modules.

## 💡 Building a "Hello World" for self-driving labs

Discover the essential principles of self-driving laboratories (SDLs) by building a "Hello World" SDL from scratch. In this asynchronous, remote course, you will build a self-driving color matcher using dimmable LEDs and a light sensor. This introduction will help you implement hardware/software communication via MQTT, database integration via MongoDB, microcontroller programming with a Raspberry Pi Pico W, and optimization via the Adaptive Experimentation (Ax) Platform. The course will conclude with an expansion of the demo to the research-relevant task of continuously logging temperature, humidity, pressure, light, and accelerometer data. For participants to complete this course within the expected timeframe (15-20 hours), intermediate proficiency in Python programming is recommended.

### 🎯 Learning Outcomes <!-- Merge LO and C/S? into table? Maybe not - implies one-to-one correspondence between the lines-->

- Describe key terms and principles of self-driving labs
- Send commands and receive sensor data over WiFi using standard frameworks such as MQTT
- Store experiment configurations and results in a MongoDB database
- Implement software on a microcontroller to adjust device power and read sensor data
- Adapt a Bayesian optimization script from packages such as the Ax Platform to iteratively suggest new colors to try <!-- Bayes opt YouTube video here, in data science, or in both? EDIT: data science -->
- Implement workflow orchestration for a color experiment using packages such as Covalent
- Modify the system to record temperature, humidity, barometric pressure, and accelerometer measurements

### 🛠️ Competencies/Skills
- Basic self-driving lab literacy
- Database management
- Workflow orchestration
- Bayesian optimization
- Microcontrollers and sensors
- Hardware/software communication

<!-- I'm not sure I like the module name/topics/LO table format. Perhaps a module name as a subheading -->

### 🧩 Modules

Module Name | Topics | Learning Outcomes
---- | ---- | ----
Running the self-driving lab demo | Database management<br>Bayesian optimization<br>Microcontrollers<br>Sensors<br>Device communication | Describe key terms and principles of self-driving labs<br>Preview an end-to-end self-driving lab<br>Set up a MongoDB account and database<br>Set up a HiveMQ account and instance<br>Upload software to a microcontroller
Blink the LEDs and read sensor data |  Microcontrollers<br>sensors | Familiarize the MicroPython programming language<br>Send commands to a microcontroller<br>Receive sensor data from a microcontroller
| Bayesian optimization for color matching | Design of experiments<br>Bayesian optimization<br>data visualization | Compare grid and random search vs. Bayesian optimization<br>Visualize optimization efficiency
| Hardware/software communication | MQTT<br>Device communication<br>Host<br>Client | Send commands to a microcontroller<br>Receive sensor data from a microcontroller
| Logging data | MongoDB<br>Database management | Set up a MongoDB account and database<br>Upload data directly from microcontroller
| Piecing the modules together | Systems design | Connect the pieces to complete the SDL demo
| Convert to a lab sensor system | Microcontrollers<br>Sensors<br>Device communication<br>Database management | Continuously log temperature, humidity, pressure, light, and accelerometer data

## 📈 Data science for self-driving labs

Unleash the power of data science in the realm of self-driving laboratories. This remote, asynchronous course empowers you to apply data science concepts to materials discovery tasks. You'll create Bayesian optimization scripts using the Ax Platform, explore advanced optimization topics, and use the Honegumi template generator to create an advanced optimization setup for a materials discovery task. Additionally, you'll learn to share your findings by uploading datasets to FigShare, creating benchmark models with scikit-learn, and hosting models on HuggingFace. The recommended prerequisite for this course is "Building a 'Hello World' for Self-Driving Labs".

### 🎯 Learning Outcomes

- Describe a materials discovery task using data science language and concepts
- Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe
- Judiciously choose an advanced optimization setup that matches a materials discovery task
- Programatically upload a completed dataset to Figshare, create a benchmark model, and host it on HuggingFace

### 🛠️ Competencies/Skills
- Data science literacy
- Bayesian optimization
- Advanced Bayesian optimization
- Workflow orchestration
- Benchmarking

### 🧩 Modules

Module Name | Topics | Learning Outcomes
--- | --- | ---
Gentle intro to Bayesian optimization | • Design of experiments<br>• Quasi-random search methods<br>• Bayesian optimization<br>• Expected improvement (EI)<br>• Ax Platform<br>• Honegumi template generator | • Describe a materials discovery task using data science language and concepts<br>• Adapt a Bayesian optimization script to find an optimal chocolate chip cookie recipe
Multi-objective optimization | • Pareto fronts<br>• Hypervolume<br>• EHVI<br>• Objective thresholds | • Explain the significance of a Pareto front<br>• Compare simple scalarization with expected hypervolume improvement<br>• Explore the effect of setting objective thresholds  <!-- incorporating domain knowledge through objective thresholds -->
Constrained optimization | • Linear constraints<br>• Nonlinear constraints<br>• Compositional constraints<br>• Order constraints | • Provide examples of materials discovery tasks with constraints<br>• Adapt a Bayesian optimization script to include constraints
High-dimensional optimization | • Curse of dimensionality<br>• SAASBO | • Explain the curse of dimensionality<br>• Compare the efficiency of expected improvement and SAASBO as a function of dimensionality
Featurization | • Domain knowledge integration<br>• Contextual variables<br>• Predefined candidates | • Explain the advantages and disadvantages of featurization<br>• Adapt a Bayesian optimization script to use predefined candidates with featurization<br>• Adapt a Bayesian optimization script to use contextual variables
Multi-fidelity optimization | • Cost-fidelity tradeoffs<br>• Knowledge gradient | • Explain the effect of cost-fidelity tradeoffs on optimization<br>• Assess the efficiency of expected improvement at fixed fidelities vs. knowledge gradient<br>• Adapte a Bayesian optimization script to use a knowledge gradient
Benchmark datasets and models | • Benchmarks<br>• Surrogate models<br>• Random forest regression<br>• FAIR data<br>• Model deployment<br>• APIs | • Programatically upload a completed dataset to Figshare<br>• Create a benchmark model with scikit-learn<br>• Host a model on HuggingFace

<!-- In intro, require Bayes opt video and user input for the different questions. This could be a GitHub discussion, comments in a PR, entry in the Canvas course, etc. -->

<!-- Mixed-variable optimization | Numerical parameters, categorical parameters |  -->

<!-- Module: Large language models for materials discovery @KevinJablonka can perhaps convert his 1-hr tutorial into this one -->

<!-- Noisy optimization | Bayesian optimization<br>Observation noise<br>Noisy expected improvement (NEI) | Explain the effect of observation noise on optimization<br>Compare the efficiency of expected improvement and NEI as a function of observation noise -->

<!-- NOTE: Moving workflow orchestration to robotics, with a covalent tutorial in hello world -->

## 🦾 Robotics for self-driving labs

Embark on a journey into the world of robotics and automation for self-driving laboratories. This asynchronous, remote course equips you with the skills to control peristaltic pumps, linear actuators, automated liquid handlers, and solid dispensers using a Pico W microcontroller, a motor driver, and the Covalent workflow orchestration package. You'll also learn to control mobile cobots using the Robot Operating System (ROS) framework and to perform spatial referencing and ID recognition via AprilTags and OpenCV. The course will conclude with a solid sample transfer workflow using Covalent, ROS, AprilTags, OpenCV, and a multi-axis robot. The recommended prerequisite for this course is *Building a "Hello World" for Self-Driving Labs*.

### 🎯 Learning Outcomes

- Implement software to control a peristaltic pump via a microcontroller and a motor driver
- Build the "Digital Pipette" and implement software to control the linear actuator
- Perform liquid transfer between vials with an automated liquid handler (Jubilee or Opentrons)
- Demonstrate control of a mobile cobot using the robot operating system (ROS) framework
- Demonstrate spatial referencing and ID lookup by using OpenCV and AprilTags
- Use ROS, AprilTags, and a multi-axis robot to perform solid sample transfer

### 🛠️ Competencies/Skills

- Motor drivers
- Automated liquid handlers
- Robotic control
- Computer vision
- Automated solid handlers

### 🧩 Modules
Module Name | Topics | Learning Outcomes
---- | ---- | ----
Controlling pumps and pipettes | Workflow orchestration<br>Microcontrollers<br>Peristaltic pumps<br>Linear actuators<br>Motor drivers | Implement software to control a peristaltic pump via a microcontroller and a motor driver<br>Build the "Digital Pipette" and implement software to control the linear actuator
Automated liquid handlers | Workflow orchestration<br>Jubilee<br>Opentrons | Perform liquid transfer between vials with an automated liquid handler (Jubilee or Opentrons)
Mobile robotics | ROS | Demonstrate control of a mobile cobot using the Robot Operating System (ROS)
Computer vision | OpenCV<br>AprilTags | Demonstrate spatial referencing and ID lookup by using OpenCV and AprilTags
Solid sample transfer | Workflow orchestration<br>ROS<br>AprilTags<br>Multi-axis robotics | Use ROS, AprilTags, and a multi-axis robot to perform solid sample transfer

## 🧑‍💻 Software development for self-driving labs

Elevate your software development skills in the context of self-driving laboratories. This asynchronous, remote course introduces software development concepts and best practices and productivity tools such as integrated development environments (IDEs) with VS Code, unit testing with pytest, continuous integration via GitHub actions, and documentation creation using Sphinx and Read the Docs. You'll also learn to deploy materials discovery campaigns on cloud servers or dedicated hardware and run offline simulations using cloud hosting. The recommended prerequisite for this course is *Building a "Hello World" for Self-Driving Labs*.

### 🎯 Learning Outcomes

- List software development best practices and corresponding benefits
- Identify productivity tools for developers that increase efficiency
- Write unit tests using tools such as pytest
- Create Python documentation using sphinx and rtd
- Implement continuous integration (CI) using tools such as GitHub actions
- Create a project template using PyScaffold
- Launch a cloud server or server on dedicated local hardware that runs a materials discovery campaign
- Run an offline simulation using cloud hosting

### 🛠️ Competencies/Skills

- Software development literacy
- Unit testing
- Documentation
- Compute hardware
- Cloud computing

### 🧩 Modules

Module Name | Topics | Learning Outcomes
---- | ---- | ----
Setting up VS Code | IDEs<br>Miniconda<br>VS Code extensions | Set up VS Code<br>Install Miniconda<br>Install VS Code extensions
Debugging in VS Code | Print statements<br>Setting breakpoints<br>Inspecting variables<br>Stepping through code<br>Debug console<br>Debug configurations | Use print statements to debug code<br>Set breakpoints<br>Inspect variables<br>Step through code<br>Use the debug console<br>Set up debug configurations
Unit testing| pytest<br>Test result interpretation<br>Debugging<br>Test-driven development | Explain the purpose of unit tests<br>Write unit tests for the light-mixing demo<br>Run and interpret unit tests to fix code<br>Explain test-driven development
Automated documentation | Markdown<br>Documentation as code<br>Sphinx<br>Readthedocs | Write documentation in Markdown<br>Explain what documentation as code means<br>Set up a readthedocs account and publish a readthedocs page
Continuous integration (CI) | Continuous integration<br>GitHub actions<br>Unit tests<br>Documentation | Explain the purpose of continuous integration<br>Set up a GitHub actions workflow<br>Run unit tests and documentation builds on GitHub actions
Project templates | PyScaffold<br>Cookiecutter<br>Project initialization<br>Project adaptation | Create a project template using PyScaffold<br>Add project content
Launching a free cloud server | Serverless computing<br>PythonAnywhere<br>Deploying Applications | Launch a free cloud server<br>Deploy a materials discovery campaign on a cloud server
On-demand cloud simulations | Cloud computing<br>Setting up an AWS account<br>AWS Lambda | Run an on-demand cloud simulation<br>Integrate a cloud simulation into a materials discovery campaign

<!-- Python packaging with PyPI | Packages<br>PyPI<br>pip<br>Twine | Explain the purpose of packages<br>Set up a PyPI account<br>Upload a package to PyPI -->
<!-- Using LLMs to enhance coding workflows via GitHub Copilot Chat | Understanding LLMs<br>GitHub Copilot Chat<br>Code Suggestions<br>Code Completions<br>Code Refactoring | Explain the purpose of LLMs<br>Explore the use of GitHub Copilot Chat -->

<!-- https://www.w3schools.com/aws/ -->

<!-- note that print statements (similarly cell evaluation outputs for notebooks) are an important beginner method of debugging -->

## 🏢 AC training lab capstone project <!-- Alternative emoji: 🏗️ -->

Turn your self-driving lab expertise into a real-world project. During this course, you will propose, design, and build a self-driving laboratory at the AC training lab equipped with education- and research-grade equipment including liquid handlers, solid dispensers, Cartesian-axis systems, and mobile robotic arms. Prior to arrival, you'll create schematic figures, write white papers, and present your proposals to a team of scientists. During a week-long in-person experience, you'll implement your proposal and document your progress. After the visit, you will share your designs, data, and documentation to contribute to the public knowledge base. The prerequisites for this course are *Building a "Hello World" for Self-Driving Labs*, *Data Science for Self-Driving Labs*, *Robotics for Self-Driving Labs*, and *Software Development for Self-Driving Labs*.

### 🎯 Learning Outcomes

- Propose a self-driving lab via a schematic figure
- Write a white paper for the self-driving laboratory
- Present the proposal to a team of scientists
- Design and build the proposed self-driving laboratory at the AC training lab
- Provide a project update with proposed next steps
- Share the designs, data, and documentation publicly

### 🛠️ Competencies/Skills

- Scientific communication
- Systems design
- Dissemination
- Interdisciplinary teamwork

### 🧩 Modules

Module Name | Topics | Learning Outcomes
---- | ---- | ----
Project proposal | Figures<br>White papers<br>Presentations | Propose a self-driving lab via a schematic figure<br>Write a white paper for the self-driving laboratory<br>Present the proposal to a team of scientists
Design and build | SDL design<br>Implementation<br>Documentation | Design and build the proposed self-driving laboratory at the AC training lab<br>Provide a project update with proposed next steps
Dissemination | Project update<br>Knowledge sharing<br>Data and documentation | Share the designs, data, and documentation publicly
