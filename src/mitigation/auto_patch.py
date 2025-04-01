import subprocess

class AutoPatcher:
    def fix_buffer_overflow(self, file_path):
        subprocess.run([
            "sed", "-i", 
            "s/strcpy/strncpy/g",  # Replace unsafe functions
            file_path
        ])
        print(f"Patched {file_path}: Replaced strcpy with strncpy")
