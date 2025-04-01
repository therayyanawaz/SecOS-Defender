#include <stdio.h>
#include <string.h>

void vulnerable_function(char *input) {
    char buffer[16]; // Small buffer to simulate overflow
    printf("Input received: %s\n", input);
    strcpy(buffer, input); // Vulnerable function (no bounds checking)
    printf("Buffer content: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }

    printf("Simulating a buffer overflow...\n");
    vulnerable_function(argv[1]);

    printf("Simulation complete.\n");
    return 0;
}
