Download
=======

1. Make sure your system is up to date using the update manager in App Store
2. Go to **Kitematic**'s [page](https://kitematic.com/), and download **Docker Toolbox**


Setup
=====

![17-23-55.png](screenshots/kitematic/osx/17-23-55.png "Install the Docker Toolbox")
Once the Docker Toolbox package is downloaded.  
Double-click to install it.

![17-25-07.png](screenshots/kitematic/osx/17-25-07.png "Installer starts")
The Docker Toolbox installer starts.  
Click _Continue_ to proceed with the installation.

![17-25-38.png](screenshots/kitematic/osx/17-25-38.png "Content")
The installer gives an overview of what is provided in the Docker Toolbox. As you can see, Kitematic is going to be installed alongside Docker, providing a desktop GUI for managing its images and containers. Click _Continue_.

![17-26-15.png](screenshots/kitematic/osx/17-26-15.png "Location")
Click on the drive where you want to install the Docker Toolbox.  
Click _Continue_.

![17-26-56.png](screenshots/kitematic/osx/17-26-56.png "Customize")
The Docker Toolbox installer provides different types of installations. Here you can select the different components that are required to run Docker images. Click _Customize_ to review the components and fine-tune your installation, or leave the installation at its defaults (what we did here) by clicking _Install_.

![17-27-31.png](screenshots/kitematic/osx/17-27-31.png "Manage")
The Docker Toolbox installer lets you choose how you would like to start managing Docker images. From here, you can either click _Continue_ to finalize the installation (and later find Kitematic within your system's Applications directory), or between the *Docker Quickstart Terminal* and *Kitematic* to readilly start managin Docker images. Click on _Kitematic_ to overview its Docker GUI.

![17-27-53.png](screenshots/kitematic/osx/17-27-53.png "Docker GUI")
The Docker GUI starts.  
Let it load.

![17-29-29.png](screenshots/kitematic/osx/17-29-29.png "Docker Hub")
Once loaded, the GUI asks you to connect to the Docker Hub to retrieve publicly available Docker images. Insert your credentials, and click _Login_.

![17-31-35.png](screenshots/kitematic/osx/17-31-35.png "Search the galaxy-rna-orkbench")
Once logged in, the GUI shows some popular Docker images readilly available for running on your system. We are interested in the _galaxy-rna-workbench_.  
Type _galaxy-rna-workbench_ in the search bar located on the top of the window to search for this image on the Docker Hub.

![17-38-11.png](screenshots/kitematic/osx/17-38-11.png "Get the galaxy-rna-workbench")
The search dialog shows the retrieved results. Select the first on the left by clicking _Create_.

![17-38-30.png](screenshots/kitematic/osx/17-38-30.png "Retrieving the image")
A connection to the Docker Hub starts to retrieve the selected image.

![17-51-08.png](screenshots/kitematic/osx/17-51-08.png "Downloading the workbench")
The workbench is being downloaded from the Docker Hub.

![21-19-09.png](screenshots/kitematic/osx/21-19-09.png "Docker container starts")
Once fully downloaded, the Docker container starts, loggin messages on the console.

![21-20-10.png](screenshots/kitematic/osx/21-20-10.png "Web preview")
A web preview of the galaxy-rna-workbench is provided next to the console log.  
Click on the preview image to open it in a browser.

![21-20-44.png](screenshots/kitematic/osx/21-20-44.png "Workbench opens in the browser")
The web preview is fully opened in your default browser, where you can readilly start working on the galaxy-rna-workbench.

![21-42-15.png](screenshots/kitematic/osx/21-42-15.png "Have a tour")
To start trying the workbench, we suggest you take an interactive tour of the galaxy workbench. The tour can be stopped at any time, and gives you an overview of what you can do through the interface, using its tools, and reusing all available workflows.  
Click on _Help -> Interactive Tours_.

![21-42-34.png](screenshots/kitematic/osx/21-42-34.png "Galaxy UI tour")
The interactive tours are listed. Click on the _Galaxy UI_ introductory tour.

![21-42-49.png](screenshots/kitematic/osx/21-42-49.png "Have fun")
Your galaxy-rna-workbench tour has started. Have fun :)  

Once finished, finalize your installation by clicking _Continue_ in the Docker Toolbox installer. This will create a Kitematic icon in your system's Applications directory, and close the Docker Toolbox installer.
