#! /bin/bash

ans_1(){
    echo "hello linux" >> ./idk.txt
}

ans_2(){
    stat -c %s ./level_1.sh
}
ans_3(){
    ls -l -a 
}
ans_4(){
 chmod 777 ./test.txt
}
ans_5(){
   sudo chown -R test:test ./test/   
}
ans_6(){
    find / -type f -size +100M
}
ans_7(){
    ln -s ./test/filler.txt symlink.txt
}
ans_8(){
    ls -l test.txt
}
ans_9(){
    diff --brief <(sort ./test/filler1.txt) <(sort ./test/filler2.txt)
}
ans_10(){
    du -h /home
}

# ans_1
# ans_2
# ans_3
# ans_4
# ans_5
# ans_6
# ans_7
# ans_8
# ans_9
ans_10