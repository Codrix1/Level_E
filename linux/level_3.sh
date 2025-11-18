#! /bin/bash

ans_1(){
    sudo ps -ef
}

ans_2(){
    pgrep nginx

}

ans_3(){
    pkill nginx
}

ans_4(){
    ps aux | grep sshd
}

ans_5(){
    ps aux --sort=-%cpu | head -5
}

ans_6(){
    sudo systemctl start ssh
}

ans_7(){
    systemctl is-enabled ssh
}

ans_8(){
    sudo systemctl restart ssh
}

ans_9(){
    journalctl -u ssh
}

ans_10(){
    top
}

# ans_1
# ans_2
ans_3
# ans_4
# ans_5
# ans_6
# ans_7
# ans_8
# ans_9
# ans_10
