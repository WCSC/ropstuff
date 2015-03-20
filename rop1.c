#include <stdio.h>

void shell() {
    printf("shell!");
    system("/bin/bash");
}

void some_func(char* string) {
    char buf[100];
    strcpy(buf, string);
}

int main(int argc, char** argv) {
    some_func(argv[1]);
    return 0;
}
