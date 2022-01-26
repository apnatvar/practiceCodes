#include <stdio.h>
#include <stdlib.h>

//this is an implementation of kadane's algorithm
int main(){
	int a[] = {1,2,3,4,5,6,7,8,9,10};
	int currentLargest = a[0];
	int xor = 0;
	int largest = 0;
	int i = 1;
	while (i<sizeof(a)/sizeof(int)){
		xor = currentLargest^a[i];
		if (currentLargest < xor){
			currentLargest = xor;
		}
		if (currentLargest > largest){
			largest = currentLargest;
		}
		i++;
	}
	printf("%d\n",largest);
	return 0;
}