#! /bin/bash

ans_1(){
 
echo $USER  
echo $UID  
}

ans_2(){
    cat /etc/*-release
    lsb_release -a
}

ans_3(){
    hostip=$(hostname -I)
    hostname1=$(hostname)
    echo "hostname: $hostname1  Ip: $hostip"
}

ans_4(){
    env
}

ans_5(){
    uname -a
}
ans_6(){
    uptime -p
}
ans_7(){
    lscpu
}
ans_8(){
    free -m
}
ans_10(){
    top
}
# ans_1
# ans_2
# ans_3 
# ans_4
# ans_5
# ans_6
# ans_7
# ans_8
# ans_10