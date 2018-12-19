#include <stdio.h>
int main(int argc, char *argv[]) {
char buffer[7];
FILE *input = fopen("runtimeBadfile", "r");
fread(buffer, sizeof(char), 35, input);
printf("Read from file: %s\n", buffer);
return 0;
}

