#include <stdio.h>
#include <string.h>

// Secure version of vulnerable_function with bounds checking
__attribute__((noinline)) void vulnerable_function(const char *input) {
    char buffer[16];
    // Safe copy using strncpy with explicit null termination
    strncpy(buffer, input, sizeof(buffer)-1);
    buffer[sizeof(buffer)-1] = '\0';
    printf("Buffer content: %s\n", buffer);
}

// Main function with ASAN compatibility
int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input>\n", argv[0]);
        return 1;
    }
    
    const char *input = argv[1];
    
    // Call the vulnerable function directly
    vulnerable_function(input);
    
    return 0;
}
