#include<stdio.h>
int main() {
char *shell = getenv("MYSHELL");
if (shell)
printf("%x\n", shell);
return 0;
}

