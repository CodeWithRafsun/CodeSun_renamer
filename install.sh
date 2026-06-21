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





CYAN="\033[0;36m"
GREEN="\033[0;32m"
RED="\033[0;31m"
RESET="\033[0m"




# =====================
# CODESUN BRAND START
# =====================


show_banner "$BASE_DIR/assets/brand.txt"



sleep 2



echo

echo -e "${CYAN}Starting CodeSun Renamer Installer...${RESET}"

sleep 1





# =====================
# Detect System
# =====================


if [ -d "/data/data/com.termux/files/usr" ]; then


    BIN_DIR="/data/data/com.termux/files/usr/bin"


    echo -e "${GREEN}✓ Termux detected${RESET}"


else


    BIN_DIR="/usr/local/bin"


    echo -e "${GREEN}✓ Linux detected${RESET}"


fi





# =====================
# Check Files
# =====================


if [ ! -f "$BASE_DIR/renamer" ]; then


    echo -e "${RED}Error: renamer launcher missing${RESET}"

    exit 1


fi






echo

echo "Installing CodeSun Renamer..."





for i in {1..30}
do

printf "█"

sleep 0.03

done



echo





# =====================
# Install Command
# =====================


cp "$BASE_DIR/renamer" "$BIN_DIR/renamer"



chmod +x "$BIN_DIR/renamer"






# =====================
# Copy Project
# =====================


INSTALL_DIR="$HOME/.renamer"



rm -rf "$INSTALL_DIR"



mkdir -p "$INSTALL_DIR"



cp -r "$BASE_DIR"/* "$INSTALL_DIR/"






# Update launcher path


sed -i "s|DIR=\"\$(cd \"\$(dirname \"\${BASH_SOURCE\[0\]}\")\" && pwd)\"|DIR=\"$INSTALL_DIR\"|" "$BIN_DIR/renamer"







sleep 1



clear




# =====================
# SUCCESS BANNER
# =====================


show_banner "$BASE_DIR/assets/success.txt"





echo
