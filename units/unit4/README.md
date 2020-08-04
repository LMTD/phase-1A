# LMTD Phase One - Unit Four - Cloud Computing & AWS
Understanding the basics of Cloud Computing using Amazon Web Services

## What is Cloud Computing?
Cloud Computing refers to the process of utilizing service platforms providing rapid access to flexible IT resources on demand. IT resources refer to things like compute power, database storage, content delivery, networking, security, management tools, application services, etc. With cloud computing, teams and businesses of all sizes can provision the necessary infrastructure, platform, or software resources they need  on-demand via the Internet with pay-as-you-go pricing.

Cloud Service Platforms like AWS, Microsoft Azure, Google Cloud, and IBM own and maintain the hardware and provide APIs to all of the various services you would need so you don't have to make large upfront investments in your own infrastructure as your business grows.

Check out this [video by AWS about cloud computing](https://youtu.be/dH0yz-Osy54) to learn more about the possibilities that utilizing the cloud has on technology services.


### Cloud Computing Benefits
#### Agility
Cloud computing makes it easier to provision new resources in a couple of minutes. This allows teams to work faster and reduce the bandwidth costs for developing, testing, and deploying larger products. 

#### Elasticity
One of the largest benefits of Cloud Computing is in its ability to help teams match resources to needs. The goal of efficiency would dictate that team's should only allocate the necessary amount of resources as needed at any given point of time. Using the cloud, this elasticity is possible.

#### Scalability
Scalability refers to the ability to handle the changing needs of a platform by adding additional resources. Scaling can happen horizontally (scaling out) or vertically (scaling up). Cloud computing makes it easy to scale applications and often allow you to do so automatically based on usage patterns.   

#### High Availability
Cloud computing helps protect the availability of your data and applications throughout common issues such as network/power outages, and application or system failures. Organizations strive to have 100% availability and Cloud providers offer "service-level agreements" to guarantee uptime close to 100% when you use systems/services under their control.

#### Fault Tolerance
Cloud providers implement systems to allow your applications to deal with failure in ways that guarantee data availability and continued operation of other services when others are down. 

#### Cost Saving
Cloud computing makes it less expensive upfront to scale out your operations. This is because you are essentially renting resources from a cloud provider rather than buying things on your own. This allows for you move from *capital* expenses to *operating* expenses where you're only buying things based on your needs versus the physical assets themselves. 

### Types of Cloud Computing Services
Offerings in the cloud are typically refered to as *services* and each service comes with its own advantages, disadvantages related to the amount of control and responsibilities over your resources you need to maintain. There are three primary types of cloud services we'll define more specifically below.

![cloud service pyramid](https://www.microsoftpressstore.com/content/images/chap1_9780135732182/elementLinks/f01xx02.jpg)

#### Infrastructure as a Service (IaaS)
Infrastructure refers to the physical hardware our applications use. IaaS refers to the process of leveraging virtualized infrastructure offered by a cloud provider. Provisioning an IaaS resource relies on a virtual machine created by the cloud service provider. In most systems you're able to customize the type of operating system and middleware you desire to use and you benefit from letting the cloud service provider manage the hardware infrastructure and networking requirements that allow you to connect to your virtual instances. IaaS offers the most flexibility allowing you to install your own software and components but you are responsible for securing, updating and maintaining that infrastructure yourself. 

#### Platform as a Service (PaaS)
In PaaS environments cloud providers manage the infrastructure for you but also provide the operating system and various middleware that enable you to build and manage your applications. PaaS services offer you less choices in your infrastructure but allow you flexibility in controlling your applications by offloading the management and control of the underlying operating systems to the cloud provider. In PaaS systems you're only responsible for managing the application that is deployed on the cloud but are subject to any changes the cloud provider makes to the underlying platform over time.      

#### Software as a Service (SaaS)
At the top of the cloud services pyramid is the Software as a Service space, wherein the cloud provider is responsible for everything including the provision of software delivered on infrastructure managed by the hosting provider. SaaS services are maintained and configured completely by a cloud host provider. In this way SaaS remove much of the IT burden from your team or company. SaaS is the least customizable and least flexible option of cloud service but allow you to access the service from a variety of locations including mobile devices. 

### Cloud Computing Deployment Models

#### Cloud
A cloud-based application is fully deployed in the cloud and all parts of the application run in the cloud. Applications in the cloud have either been created in the cloud or have been migrated from an existing infrastructure to take advantage of the benefits of cloud computing. Cloud-based applications can be built on low-level infrastructure pieces or can use higher level services that provide abstraction from the management, architecting, and scaling requirements of core infrastructure.

#### Hybrid
A hybrid deployment is a way to connect infrastructure and applications between cloud-based resources and existing resources that are not located in the cloud. The most common method of hybrid deployment is between the cloud and existing on-premises infrastructure to extend, and grow, an organization's infrastructure into the cloud while connecting cloud resources to internal system. 

#### On-Premise
Deploying resources on-premises, using virtualization and resource management tools, is sometimes called “private cloud”. On-premises deployment does not provide many of the benefits of cloud computing but is sometimes sought for its ability to provide dedicated resources. In most cases this deployment model is the same as legacy IT infrastructure while using application management and virtualization technologies to try and increase resource utilization.


### What is AWS
![What is AWS](https://i0.wp.com/www.thedevcoach.co.uk/wp-content/uploads/2019/11/Screenshot-2019-11-13-at-06.48.23.png?w=1418&ssl=1)

AWS stands for Amazon Web Services. AWS is a range of computing products that allow you to operate tasks in the cloud, on demand. And currently, AWS have the biggest service offering of the cloud market, so you have everything from databases, to event queues, to basic website hosting.

#### What is a Web Service?


### Core AWS Services
#### EC2
EC2 is the flagship AWS product, and it’s where most of current AWS revenue comes from. EC2 stands for Elastic Compute Cloud think of it as a way to run a computer in the cloud. You can launch Linux machines, or Windows machines all on top of EC2. On EC2 you can run many different types of workloads. You can install WordPress, to run a website. Or you can install a database and store data, all directly on an EC2 machine. In fact, nearly everything you can imagine can be ran on EC2.

#### IAM
AWS IAM is how you manage permissions and access in AWS. In order to launch your EC2 instance from before, you need to have a user that has the appropriate access to do so. And to get access you need to use AWS IAM. Within IAM you’ve got: users, groups, roles and policies and they’re all related somehow.

But, IAM is deceptively complex. IAM isn’t only how users get access to do things in AWS, it’s also how you grant machines to talk to each other. For instance, if we look at EC2 again, an EC2 machine can be assigned a role. And that role then governs what that EC2 can and can’t do.

#### S3
S3 is another deceptively versatile service, which allows you to store files in a flexible way. S3 can be used to host websites, store assets such as images, and even log files for your application. If you ever need simple persistence for files, S3 is probably the answer. Many services in AWS are built around S3. So it makes sense to learn S3 first

### Other Important AWS Services
* CloudWatch — The built-in AWS monitoring tool.

* Route 53 — Domain purchasing and DNS routing. Allows you to point your website or server to a domain name.

* RDS — The AWS hosted database solutions. Has a range of databases from SQL to document-based.

* CloudFormation — AWS built-in Infrastructure as Code. Create resources by writing your infrastructure as a JSON template and tell AWS to create it.

### Connecting to AWS
#### AWS Management Console
Access and manage Amazon Web Services through the AWS Management Console, a simple and intuitive user interface. You can also use the AWS Console Mobile Application to quickly view resources on the go.

#### AWS Command Line Interface
The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

#### Software Development Kits
AWS Software Development Kits (SDKs) simplify using AWS services in your applications with an Application Program Interface (API) tailored to your programming language or platform.

### AWS Exam / Certifications

![AWS Exams](https://i1.wp.com/www.thedevcoach.co.uk/wp-content/uploads/2019/11/awsexams.png?w=1520&ssl=1)

## Resources
* [Overview of Amazon Web Services](https://d1.awsstatic.com/whitepapers/aws-overview.pdf)

* [What is Cloud Computing - AWS](https://aws.amazon.com/what-is-cloud-computing/)

* [Understanding Cloud Computing Terminology](https://www.microsoftpressstore.com/articles/article.aspx?p=2979073)

* [Where (and how) to start learning AWS as a beginner](https://www.thedevcoach.co.uk/start-learning-aws-beginner/)

* [Difference Between APIs and Web Services](https://medium.com/@programmerasi/difference-between-api-and-web-service-73c873573c9d)

