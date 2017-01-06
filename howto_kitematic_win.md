# Galaxy RNA workbench on Kitematic for Windows

This how-to will guide you through the steps that are needed to run the Galaxy RNA workbench on Windows by setting up [Kitematic](https://kitematic.com), which provides a graphical user interface to run Docker containers stored on DockerHub


## Installation prerequisites

Before proceeding, make sure your system is up to date using Microsoft's Windows Update.  
Finally, go to Kitematic's [page](https://kitematic.com/), and download the *Docker Toolbox*.  

## Installation procedure

1. Place the downloaded installer where it is more convenient for you. Here we placed it on the Desktop for clarity.  
  Once the Docker Toolbox package is fully downloaded, double-click to proceed to its installation.  
  ![01.png](screenshots/kitematic/win/01.png "Install the Docker Toolbox")

2. The Docker Toolbox installer starts. Click _Next_ to proceed with the installation.  
  ![02.png](screenshots/kitematic/win/02.png "Installer starts")

3. Set the location where you want to install the Docker Toolbox. Click _Next_.  
  ![03.png](screenshots/kitematic/win/03.png "Location")

4. The installer gives an overview of what is provided in the Docker Toolbox. As you can see, Kitematic is going to be installed alongside Docker, providing a desktop GUI for managing its images and containers. Click _Next_.  
  ![04.png](screenshots/kitematic/win/04.png "Content")

5. Leave the post-installation tasks to their default to obtain all Docker Toolbox's desktop icons. Click _Next_.  
  ![05.png](screenshots/kitematic/win/05.png "Post-installation setup")

6. Review the provided installation location and components. Click _Install_.  
  ![06.png](screenshots/kitematic/win/06.png "Review installation")

7. The installation completes by creating all Docker Toolbox's icons in the defined location. By leaving the settings at their defaults, these will appear on the desktop. Click _Finish_.  
  ![07.png](screenshots/kitematic/win/07.png "Finish the installation")

8. The Docker GUI starts. Let it load.  
  ![08.png](screenshots/kitematic/win/08.png "Docker GUI")

9. Once loaded, the GUI asks you to connect to the Docker Hub to retrieve publicly available Docker images.  
  Insert your credentials, and click _Login_.  
  ![09.png](screenshots/kitematic/win/09.png "Docker Hub")

10. Once logged in, the GUI shows some popular Docker images readilly available for running on your system.  
  We are interested in the _Galaxy RNA workbench_. Type _galaxy-rna-workbench_ in the search bar located on the top of the window to search for this image on the Docker Hub.  
  ![10.png](screenshots/kitematic/win/10.png "Search the galaxy-rna-workbench")

11. The search dialog shows the retrieved results. Select the first on the left by clicking _Create_.  
  ![11.png](screenshots/kitematic/win/11.png "Get the galaxy-rna-workbench")

12. A connection to the Docker Hub is started, and the workbench is retrieved from the Docker Hub.  
  ![12.png](screenshots/kitematic/win/12.png "Downloading the workbench")

13. Once fully downloaded, the Docker container starts, loggin messages on the console. A web preview of the Galaxy RNA workbench is provided next to the console log. Click on the preview window to open it in a browser.  
  ![13.png](screenshots/kitematic/win/13.png "Docker container starts")

14. The web preview is fully opened in your default browser, where you can readilly start working on the workbench.  
  The opening page shows some useful options to configure Galaxy, install new tools, or try the workbench through a guided tour: an interactive demo showing the usage of preloaded tools to carry out a simple workflow experiment.  
  Tours can be stopped at any time, and provide you an overview of what can be done through Galaxy, using its tools, and reusing all available workflows.  
  ![14.png](screenshots/kitematic/win/14.png "Workbench opens in the browser")

15. To have an introductory tour on the Galaxy interface, Click on _Help -> Interactive Tours_, and select the _Galaxy UI_ tour.  
  Your Galaxy RNA workbench tour has started. Have fun :)  
  ![15.png](screenshots/kitematic/win/15.png "Introductory tour")

