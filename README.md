# Kurooto
Official Repository of Kurooto, The AI which powers all of the Armors of Sumangalam Avtar Sharma
For more info, contact at sumangalam_avtar@yahoo.com
## Prerequisites
* **Python Version 3.9 with pip installed** and Python added to **Environment Variables**
# Installation Procedure (WINDOWS ONLY)
1. Download the release from [here](https://github.com/cursedsoulofgods/Kurooto/archive/master.zip)
2. Once downloaded, extract the resulting archive in a suitable location
3. Open the resulting folder
    1. Open setup_files folder and run vc_redist.x64.exe to install required C++ libraries
    2. Once the installation is complete, restart your computer for best chances of success
    3. Now open up the main root installtion folder, that is Kurooto-master
    4. Now press the following combination, Shift+SMB (Secondary Mouse Button, default is Right Mouse Button) to open up advanced Right Click Context Menu.
    5. In the resulting menu, select **Open Powershell Window here** or **Open Command Prompt here**
    6. Step 2 should open up a Console window which would be directed to your current Kurooto Installation path.
    **Note** - *If the following doesn't work for you, one can just launch a cmd window and cd to the Installation Path.*
    7. In the console window, execute the following commands
        1. `python -m venv venv\` This will create a virtual Environment in the directory           inside the folder venv.
        2. `venv\scripts\activate.bat` This will activate the environment
        3. `pip install -r requirements.txt` This would install the required packages.             **This will take quite a while as the required packages will be downloaded**
## Setting up Email Services and Microphone
1. Once the above mentioned steps have been performed, user settings can now be set.
    1. Start by opening up **setup_files** folder and open up **Command Prompt or           Powershell Window there** *(for how to do so, refer to step 3(i) and 3(ii))*
    **Note** - *If the following doesn't work for you, one can just launch a cmd window     and cd to the setup_files folder path.*
    2. Now execute the following command - `python set_email.py`
    3. Follow the instructions and enter your Gmail ID
    4. Once the execution of the script is complete, your email address would be safely     stored in a file inside the user folder.
    5. Now execute the following command - `python set_threshold.py`
    6. Follow the instructions and enter the required amount of Threshold
    **Threshold refers to the amount of pressure required for your voice to be detected,    the higher the threshold, the louder your voice will need to be and the more the        backgound noises will be avoided. Having a higher threshold value is better in noisy    environments**
    7. Now in the same command prompt, execute the following command to install PyAudio - `pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl`
