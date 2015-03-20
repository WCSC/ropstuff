#include <stdio.h>

void not_shell() {
    printf("You wish it was /bin/bash");
    system("/bin/ls");
}

void some_func(char* string) {
    char buf[100];
    strcpy(buf, string);
}

int main(int argc, char** argv) {
    some_func(argv[1]);
    return 0;
}
