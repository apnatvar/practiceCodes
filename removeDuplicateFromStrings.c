#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

	char inputString[100];
	printf("Enter String to remove duplicate from\n");
	scanf("%[^\n]s", inputString); //changing the delimiter to \n so that we can input a line
	//does not differentiate between 'A' or 'a' hence
	//Amazing would be modified as Amazing
	
	int inputIndex = 0;
	int outputIndex = 0;
	int tempIndex;
	int flag;
	char modifiedInputString[100];

	while (inputIndex < strlen(inputString)){
		tempIndex = 0;
		flag = 1;
		while (tempIndex < outputIndex){ //to check if the new character it is in the original string
			if (modifiedInputString[tempIndex] == inputString[inputIndex]){
				flag = 0;
				break;
			}
			tempIndex++;
		}
		if (flag){
			modifiedInputString[outputIndex++] = inputString[inputIndex]; //adding to modified string
		}
		inputIndex++;
	}

	printf("%s", modifiedInputString);
	return 0;

}