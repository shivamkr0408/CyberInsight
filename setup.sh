#!/bin/bash
# Eye4Eye Setup Script
# Installs all dependencies and prepares the environment

cat << "EOF"
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡅⠀⠀⠀⠀⠀⠀⠀⡄⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⣰⠀⠀⠆⠀⠀⢀⠌⡄⡌⠁⠀⠀⠠⠁⠀⠀⠀⢀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠚⡔⢣⠀⡰⢀⡀⠴⣡⠚⠠⠀⠀⢀⡐⠃⠀⢀⡄⠎⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⢰⠸⡤⠋⡠⢧⠹⡔⢫⠜⣱⢂⡭⢄⠲⣌⢣⠜⡰⡘⢦⢈⡀⠄⠒⠀⠀⠀⠀⠀⠀⡀⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢀⠠⣐⠎⡜⡈⡱⡘⡕⡱⢌⠳⣌⠧⢪⠑⠮⠔⠎⠳⡜⣬⠚⣥⡙⢆⡣⢜⢣⠒⣆⠲⡐⢆⢣⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢑⠦⡠⢄⠤⣀⢖⡰⣊⠬⡓⣌⠦⣈⠲⣡⠃⠜⠂⢉⠠⠀⠄⠂⠄⢂⠐⡀⠂⠄⢀⠉⡐⠪⠱⣌⢣⢎⡹⣐⠣⡝⣠⢀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠑⢎⠲⡡⢎⠴⣡⠣⣕⠪⠜⠀⡁⠀⠄⠂⠌⡀⠂⠡⢈⠐⠈⡀⠂⠄⠁⢂⠀⠂⠄⠂⡁⠀⡉⠂⠵⣈⠳⣘⠤⣋⢜⡡⢆⣀⣀⢂⡔⠲⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠢⠔⢲⡐⠮⣌⢣⡑⢎⡲⠅⠃⠠⢀⠂⡐⠠⠁⠌⠐⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠈⠐⢀⠂⠄⠁⠐⡈⠄⡈⠑⢬⡑⠪⡆⣙⠆⠶⣈⠒⣈⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣐⠣⡜⢣⠜⣢⠙⠈⡀⠐⡈⠐⡀⠂⠄⠁⠀⠀⠀⠀⠀⠂⠁⠀⠂⠁⠀⠀⠀⠂⠀⠀⠀⠀⠀⠌⠠⢁⠠⠀⠐⠈⡀⠘⢅⠎⡰⢌⠥⠡⠓⢆⣒⠲⠌⠃⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⢀⡀⣀⢀⡀⡥⢰⣉⠦⡙⣌⢣⠚⠀⠠⠁⠄⠡⢀⠡⠐⠀⠀⠀⠀⠀⠀⠈⣀⢠⡔⠤⠀⠀⠀⠈⠀⡀⠀⠁⠀⠄⠀⠀⠀⠂⠠⠁⠌⠀⠀⡀⠀⠉⡖⢢⡙⢤⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⢉⡐⡣⢜⢢⡙⡄⠃⠁⠌⠠⠁⡌⢐⠠⠂⠀⠀⠠⠀⠁⠀⡀⠀⠀⠉⠃⠀⠀⡀⢀⠂⠁⠀⠈⠀⠠⠀⠐⠈⠀⠀⠁⡈⠐⡈⠄⠀⢂⠐⠈⢣⠜⣢⢙⠢⢄⡀⠄⠀⠀⣀⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⢁⡔⢎⠲⣉⠎⠂⠁⠠⡀⢁⡈⠤⠑⡠⠊⡄⠁⠂⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠂⠀⠀⠠⠐⠈⠀⠂⠀⠀⡀⠀⠀⠀⠀⠠⠁⠄⠂⡁⠀⠌⠐⡀⠳⢄⢋⠖⡠⣘⡈⠣⠙⠂⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠠⠊⢠⡘⣌⠳⠀⢠⠈⠄⢁⠐⡄⠢⢌⠱⡠⢃⠄⠀⠀⠀⠈⠀⢀⠀⠀⠀⠀⠂⠀⠀⡀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠀⠀⡡⢈⠀⠠⠈⠄⠀⠐⡀⠫⢄⢫⠔⣡⠆⡄⠁⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⡀⡍⢦⠱⡌⠁⡈⠄⢈⠐⡄⠣⡔⢡⢊⡥⣓⢎⠀⠀⠀⢀⠀⠄⠀⢀⠈⠀⠁⠀⠀⠄⠀⠀⠀⡀⠈⠀⠀⡀⠁⢀⠀⠁⠀⠀⠀⠀⠰⢡⠈⡄⠁⠂⠄⠂⠠⠀⣋⠦⡙⡔⢪⠔⡢⢄⡀⣀⢀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠁⠤⠒⢭⠒⡍⠆⠃⠠⠀⠐⢀⠢⢁⠨⡑⡩⢆⣏⠲⡍⡞⠀⠀⠀⠀⠀⢀⠠⠀⠀⠌⠀⠀⠀⡀⠀⠠⠀⠀⠀⠄⢁⣀⠀⠀⠀⠂⠀⠁⠀⠀⣳⢢⢅⡘⠤⠈⠐⡈⠄⠁⢀⠎⡱⢜⡡⠊⠑⠒⠘⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠐⡠⢔⢪⠑⡈⠐⠌⠠⠁⠐⠠⡐⠌⡂⡼⣱⢫⡜⣣⠝⡼⡀⠀⠠⠀⠈⠀⠀⠠⠀⠀⠁⠀⠀⠀⠀⠄⠀⠐⠀⡐⠀⠀⠐⠀⠀⠀⠀⠀⡐⠀⡭⣕⠺⣜⢢⠁⡂⠀⠂⠄⡂⢖⠨⡐⠡⠋⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⢁⠂⡔⢪⠔⠉⠤⡘⠤⢁⠘⡀⢀⠈⠥⡐⠡⢘⡱⢣⠳⡜⢥⢫⡕⢣⠀⠀⡀⠄⠐⠀⠀⠀⠀⠀⢀⠲⠄⠤⠠⢄⠰⢀⠐⠌⠁⠠⢀⠀⠀⠂⠀⠀⢰⡱⢎⡝⢮⢣⢇⠄⡀⢁⠤⠉⠢⡑⢬⢡⠡⣄⠠⣁⢀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠌⡐⠀⠎⢌⠡⢌⡘⡡⠜⡰⠡⡐⠰⠀⢂⠑⡈⢅⠨⣕⢫⣓⡹⢎⡣⢞⡱⣂⠐⠀⡀⠀⠀⡀⠀⠁⠆⠀⠌⢘⠀⢃⠂⠎⠀⠄⠀⠀⠀⠀⠀⢀⠀⢀⠶⣙⠮⣜⣣⠯⣜⠠⢀⢃⡌⡲⢍⠭⣰⣃⠳⠌⠳⠄⠆⠜⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠌⠀⠀⠤⣉⠦⣑⠪⡔⣡⢣⡑⢣⠱⣡⢋⡔⡢⢄⡒⠄⢩⠖⣥⢛⡬⢳⣍⢳⢭⣆⡐⠀⠐⠀⠐⠀⠀⡀⠀⠀⠄⠈⠀⠅⡐⠈⠀⠀⠁⠀⠠⠀⠂⣠⢋⡞⣥⢛⡴⢣⡝⠢⣠⢒⠵⣊⡥⢖⡭⢤⣀⡀⠂⠁⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⠀⡈⠀⢂⡀⠄⢁⠓⡨⠄⢣⡘⠥⠓⠦⠳⠸⠡⢏⡜⡲⣄⠛⡴⣋⣜⢣⢎⢧⡛⡼⡰⣄⠀⠤⠁⠀⢀⠀⠀⠀⠀⠀⠐⠀⠐⠄⠀⠄⢀⠌⠀⢀⡴⣃⠯⡜⢦⢫⡜⢣⣊⡞⢴⡋⠞⠁⣀⠢⢀⠌⠁⠈⠂⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢀⠀⠐⠀⠀⠍⠂⠘⠀⠐⠂⠘⠤⣁⢂⠡⢆⠳⡐⠎⣑⠪⢛⣦⢕⡮⣙⢎⠮⣕⢣⡽⢢⠳⣄⣀⠀⠀⠠⠁⠈⠀⠀⡄⠐⠀⠐⠡⠈⢂⡤⣊⠷⡸⢥⡛⣜⢧⣳⡝⣯⢷⣙⡫⠖⠞⠤⠆⣅⠂⠀⠠⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠂⠐⠠⠀⠀⡀⠌⠀⠅⠢⢑⠦⣉⠧⢬⡑⠫⡷⣮⣗⣮⢳⣜⢫⡝⢦⣋⢾⡱⢆⡤⣄⣁⣀⣈⡐⢬⠤⣔⡲⢭⢳⡼⣡⢟⡹⣖⡽⣞⢧⣳⢫⠓⠦⡛⠍⡑⠨⠐⡄⠂⡌⠑⠠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠠⠐⠀⠠⠀⡀⠀⠀⠄⠂⠥⠀⢊⡐⠭⡒⠭⣓⠬⣝⢾⣿⣿⣞⡷⣚⣧⣹⢶⣙⢮⡵⣚⢦⡳⢎⡵⣫⢞⡼⣱⣏⣷⣺⣽⣾⢿⣭⢷⣛⡚⠐⠣⠍⡒⠡⠘⡠⢁⠢⠸⡷⠌⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⠥⠀⠀⠈⠀⠀⠀⡁⠂⠔⣂⠈⡑⢎⡳⢣⠟⣰⢒⢦⡝⣿⠾⣿⣿⡿⣿⣿⡿⣿⢿⣿⡿⣿⣿⣿⣿⠿⠿⣛⢯⢣⠳⡜⢆⢦⡹⣙⠒⠦⢤⣁⠤⡰⢀⠣⡑⢠⠈⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠐⠈⠐⠄⡊⠄⠑⠢⢄⢂⠱⣄⢫⢄⠏⡼⣡⢏⠶⣩⡗⣻⢼⣿⣝⡳⣎⢿⣹⡛⣯⡝⣎⢣⢲⡣⢍⠜⢢⠝⢪⡑⢭⠚⣤⢓⡬⣙⣪⡶⣌⠇⠡⢊⠀⡔⡡⢊⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡈⢒⠤⡠⠜⡄⢆⣣⠘⡜⢲⢱⣊⠳⣥⢋⠷⣿⣷⢫⣷⣽⡾⣥⢛⡴⡹⣌⠇⣣⠱⣋⠖⡥⢛⠴⣈⠢⡋⡴⢃⠒⠥⠎⡑⢄⢲⡑⢃⠰⠌⠡⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                Eye4Eye - Attack Surface Mapper
                        Setup Script
========================================================================
EOF
echo ""

# Check Python version
echo "[*] Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "[!] Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check pip
echo "[*] Checking pip..."
pip3 --version

if [ $? -ne 0 ]; then
    echo "[!] pip is not installed. Installing pip..."
    sudo apt-get install python3-pip -y
fi

# Install Python dependencies
echo ""
echo "[*] Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "[+] Python dependencies installed successfully!"
else
    echo "[!] Failed to install some dependencies. Please check the error messages above."
    exit 1
fi

# Check for nmap (optional)
echo ""
echo "[*] Checking for nmap (optional but recommended)..."
if command -v nmap &> /dev/null; then
    echo "[+] nmap is installed: $(nmap --version | head -n 1)"
else
    echo "[!] nmap is not installed."
    echo "    For advanced port scanning, install nmap:"
    echo "    Ubuntu/Debian: sudo apt-get install nmap"
    echo "    macOS: brew install nmap"
    echo "    Fedora/RHEL: sudo dnf install nmap"
fi

# Make scripts executable
echo ""
echo "[*] Making scripts executable..."
chmod +x eye4eye.py
chmod +x examples.py

# Create output directory
echo "[*] Creating output directory..."
mkdir -p output

# Test import
echo ""
echo "[*] Testing installation..."
python3 -c "
import dns.resolver
import requests
import plotly
import networkx
import colorama
import pyfiglet
print('[+] All core modules imported successfully!')
"

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "  ✓ Setup Complete!"
    echo "========================================="
    echo ""
    echo "You can now run Eye4Eye:"
    echo "  python3 eye4eye.py --help"
    echo "  python3 eye4eye.py example.com"
    echo ""
    echo "For examples:"
    echo "  python3 examples.py"
    echo ""
    echo "Read the documentation:"
    echo "  cat README.md"
    echo "  cat QUICKSTART.md"
    echo ""
else
    echo ""
    echo "[!] Setup completed with errors."
    echo "    Please check the error messages above."
    exit 1
fi
