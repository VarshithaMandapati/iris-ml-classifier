\
// iris_display.c
// Basic C program to display output from ML model

#include <stdio.h>

int main() {
    FILE *file;
    char line[256];

    file = fopen("iris_output.txt", "r");
    if (file == NULL) {
        printf("Error: Could not open output file.\n");
        printf("Run `python iris_classifier.py` first to generate iris_output.txt\n");
        return 1;
    }

    printf("=== Iris Classification Result ===\n");

    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }

    fclose(file);
    return 0;
}
