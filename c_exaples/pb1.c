#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	char seq[1000];
	scanf("%s", seq);

	int length = strlen(seq);

	printf("The length was: %d\n", length);

	int gc = 0;
	for (int i = 0; i < length; i++) {
		if(seq[i] == 'G' || seq[i] == 'C') {
			gc++;
		}
	}

	printf("The GC content is: %f\n", 100.0*gc/length);
}
