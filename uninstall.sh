#!/usr/bin/env bash


clear


BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"



show_banner(){

FILE=$1


if [ -f "$FILE" ]; then


python3 - <<EOF

with open(
"$FILE",
"r",
encoding="utf-8"
) as f:

    print(
        f.read()
        .encode()
        .decode("unicode_escape")
    )

EOF

fi

}





GREEN="\033[0;32m"
CYAN="\033[0;36m"
RED="\033[0;31m"
RESET="\033[0m"





# Brand Banner


show_banner "$BASE_DIR/assets/brand.txt"


sleep 2




echo

echo -e "${CYAN}Starting CodeSun Renamer Uninstaller...${RESET}"

sleep 1





# Detect system


if [ -d "/data/data/com.termux/files/usr" ]; then


    BIN_DIR="/data/data/com.termux/files/usr/bin"


    echo -e "${GREEN}✓ Termux detected${RESET}"


else


    BIN_DIR="/usr/local/bin"


    echo -e "${GREEN}✓ Linux detected${RESET}"


fi






echo


echo "Removing CodeSun Renamer..."



for i in {1..25}
do

printf "█"

sleep 0.03

done



echo






# Remove command


if [ -f "$BIN_DIR/renamer" ]; then


    rm "$BIN_DIR/renamer"


    echo -e "${GREEN}✓ Command removed${RESET}"


else


    echo -e "${RED}Command not found${RESET}"


fi






# Remove project


INSTALL_DIR="$HOME/.renamer"



if [ -d "$INSTALL_DIR" ]; then


    rm -rf "$INSTALL_DIR"


    echo -e "${GREEN}✓ Project files removed${RESET}"


else


    echo -e "${RED}Project files not found${RESET}"


fi





echo



echo -e "${GREEN}"
echo "===================================="
echo " CodeSun Renamer Removed Successfully"
echo "===================================="
echo -e "${RESET}"
