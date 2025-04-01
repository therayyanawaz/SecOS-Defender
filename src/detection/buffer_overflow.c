#include <stdio.h>
#include <string.h>
#include <sanitizer/asan_interface.h>

// Secure version of vulnerable_function with bounds checking
__attribute__((noinline)) void vulnerable_function(const char *input) {
    char buffer[16];
    // Safe copy using strncpy with explicit null termination
    strncpy(buffer, input, sizeof(buffer)-1);
    buffer[sizeof(buffer)-1] = '\0';
    printf("Buffer content: %s\n", buffer);
}

// ASAN-friendly main function
int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input>\n", argv[0]);
        return 1;
    }
    
    const char *input = argv[1];
    size_t input_len = strlen(input);
    
    // AddressSanitizer: Detect memory errors at runtime
    void *fake_stack = __asan_allocate_fake_stack();
    vulnerable_function(input);
    __asan_deallocate_fake_stack(fake_stack);
    
    return 0;
}
