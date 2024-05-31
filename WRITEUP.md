# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

Azure Virtual Machine is Infrastructure as a Service, giving you infrastructure (virtual machines) for you to install and customize yourself.
Azure App Service is Platform as a Service, giving you a platform (with a built-in runtime), you just need to put the code in and run it.

Advantages of Azure Virtual Machines:
1. Manageability: You possess complete authority over the underlying operating system, allowing for tailored configurations and the capability to execute customized software.
2. Flexibility: Azure VMs provide the flexibility of virtualization without the need to acquire and manage physical hardware. This allows you to run applications, regardless of their programming language, framework, or technology stack, with ease.
3. Familiarity: For those transitioning from an on-premises environment to Azure and are new to the platform, understanding the intricacies of Azure Virtual Machines is generally more straightforward when compared to alternative hosting solutions.

Disadvantages of Azure Virtual Machines:
1. Manageability: While we've highlighted the manageability of virtual machines as an advantage, some individuals may view it as a drawback due to the increased need for hands-on management. It's essential to bear in mind that virtual machines entail responsibilities such as OS maintenance, updates, and software upkeep, which can be manageable for a small number of VMs but become cumbersome when dealing with a larger fleet of them.
2. Potentially higher costs: Instead of dedicating your efforts primarily to constructing and sustaining your application, you must consistently factor in the manageability of your VMs. This can lead to increased expenses as you require infrastructure engineers to focus on VM maintenance.

Advantages of Azure App Service:
1. Simplified management: Microsoft Azure takes care of the underlying infrastructure allowing you to focus on your application.
Immediate deployment: App Service offers fast deployment and continuous integration with tools like Git, GitHub, and Azure DevOps.
2. Cost efficiency: A single App Service plan can contain multiple applications as long as the plan has enough resources to handle the increasing load.

Disadvantages of Azure App Service
1. Control: If you need specific controls over your infrastructure, then Azure VMs is your best choice. You only have a few options with Azure App service. 
2. Compatibility: App Service only offers specific languages. If you have a language not supported by App Service, VMs is your choice.
3. Potentially higher costs: If you need to upgrade a portion of your App tier, such as storage, you must upgrade to the next plan tier. This may result in higher costs and underutilized resources. 


### Assess app changes that would change your decision.

the size of this application is small with simple functions(only CRUD). I only need to push my code and run it.
To save the cost, I choose app service to deploy application. mothly cost for VM is 137.24$ but for App service is 54.75$.
Besides, when I choose app service, I have less control over infrastructure and settings. 

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
URL: https://azure-prj1.azurewebsites.net/