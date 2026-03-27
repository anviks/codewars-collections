#include <stdio.h>
#include <string.h>

char* filterRefsOut(char* source) {
    int i = 0, in_ref = 0;
    while (i < strlen(source)) {
        if (source[i] == '[') in_ref = 1;
        if (source[i] == ']') in_ref = 0;
        if (in_ref || source[i] == ']') {
            memmove(source + i, source + i + 1, strlen(source + i));
            i--;
        }
        i++;
    }
    return source;
}

int main() {
    char* article = strdup("wadm tikm chl[100] nizl [3]");
    filterRefsOut(article);
    printf("%s\n", article);

    return 0;
}
