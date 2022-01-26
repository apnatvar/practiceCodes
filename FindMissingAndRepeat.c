#include <stdio.h>
#include <stdlib.h>

int main(){
	int n = 10;
	int unsortedGivenArray[] = {5,4,6,2,7,8,0,9,3,3};
	int *arr=(int*)calloc(n,sizeof(int));
	int i = 0;
	while (i < 10){
		arr[unsortedGivenArray[i]]++;
		i++;
	}
	i = 0;
	int missingElement;
	int doubleElement;
	while (i < 10){
		if (arr[i]==0){
			missingElement = i;
		}
		if (arr[i]==2){
			doubleElement = i;
		}
		i++;
	}
	printf("The Missing Element is %d\n",missingElement);
	printf("The Double Element is %d\n",doubleElement);
	return 0;
}