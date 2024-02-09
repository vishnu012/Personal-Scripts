#!/bin/bash

echo "Do you want to uninstall the software? (y/n)"
read response

if [ "$response" == "y" ]; then

  ## Remove the bloat
	sudo apt purge redshift -y
	sudo apt purge libreoffice-core -y
	sudo apt purge libreoffice-common -y
	sudo apt purge transmission-gtk -y
	sudo apt purge hexchat -y
	sudo apt purge baobab -y
	sudo apt purge seahorse -y
	sudo apt purge thunderbird -y
	sudo apt purge rhythmbox -y
	sudo apt purge pix -y
	sudo apt purge simple-scan -y
	sudo apt purge drawing -y
	sudo apt purge gnote -y
	sudo apt purge xreader -y
	sudo apt purge onboard -y
	sudo apt purge gnome-calendar -y
	sudo apt purge celluloid -y
	sudo apt purge gnome-logs -y
	sudo apt purge gnome-power-manager -y
	sudo apt purge onboard -y
	sudo apt purge warpinator -y
    sudo apt purge hypnotix -y
    sudo apt purge xfce4-dict -y
    sudo apt purge webapp-manager -y
    sudo apt purge catfish -y

	sudo apt autoremove -y && sudo apt clean 

    echo "Linux mint debloated successfully."
else
    echo "No software uninstalled."
fi
