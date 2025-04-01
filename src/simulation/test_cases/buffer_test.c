#include <stdio.h>
#include <string.h>

extern void vulnerable_function(const char *input);  // From buffer_overflow.c

void test_buffer_overflow() {
    const char *payload = "A"; // 256 'A's
    printf("[TEST] Triggering buffer overflow...\n");
    vulnerable_function(payload);
    printf("[TEST] Overflow test completed\n");
}

int main() {
    test_buffer_overflow();
    return 0;
}
