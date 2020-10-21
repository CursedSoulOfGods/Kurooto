import os

threshold_loc = os.path.normpath((os.path.join(os.path.dirname(__file__), "user/settings")))
threshold_loc = threshold_loc.replace("\\setup_files", "")
threshold = input("Set threshold value here! Value should be between 500 to 5000. \nFor optimal results keep value between 2750 to 4000\n Enter your threshold value -\n")
threshold = int(threshold)
if 500<= threshold <=5000:
    write_threshold = open(threshold_loc + "\\threshold.KRT", 'w')
    threshold = str(threshold)
    write_threshold.write(threshold)
    write_threshold.close()
    print("Threshold set to", threshold)