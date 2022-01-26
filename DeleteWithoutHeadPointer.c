#include <stdio.h>
#include <stdlib.h>

typedef struct delStruct delstruct;
struct delStruct{
	int data;
	delStruct* next;
}

void deleteNode(delStruct* deleteThis){
	delStruct* temp;
	while (deleteThis->next->next!=NULL){
		deleteThis->data = deleteThis->next->data;
		deleteThis->next = deleteThis->next->next;
		deleteThis = deleteThis->next;
	}
	deleteThis->data = deleteThis->next->data;
	temp = deleteThis->next;
	deleteThis->next = NULL;
	free(temp);
}
int main(){
	//printList();
	//deleteNode(randomAddress);
	//printList();
	return 0;
}