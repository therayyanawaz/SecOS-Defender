#include <stdio.h>

int main() {
    char buffer[10];
    gets(buffer); // Vulnerable function, no bounds checking
    printf("%s\n", buffer);
    return 0;
}
