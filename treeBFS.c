#include <stdio.h>
#include <stdlib.h>
//this is only one function to check if a binary tree is in fact a BST

//this is the expected structure of a BST.
//even if it is much different this code will porbably verify the same
typedef struct BST BST;
struct BST{
	int currentNodeValue;
	BST *leftNode;
	BST *rightNode;
};
BST *head = NULL;//will not be null in a full program
//I have merely defined a structure but not built a BST

BST *BFSQ[1000]; //will store the final BST order
int qIndex = 0;
void BFSonBST(){
	static int pickThisNode = 0;
	if (BFSQ[pickThisNode]->leftNode != NULL){
		BFSQ[qIndex] = BFSQ[pickThisNode]->leftNode;
		qIndex++;
	}
	if (BFSQ[pickThisNode]->rightNode != NULL){
		BFSQ[qIndex] = BFSQ[pickThisNode]->rightNode;
		qIndex++; 
	}
	pickThisNode++;
	if (BFSQ[pickThisNode] != NULL)BFSonBST(); //recursive calls to evaluate until the end
}

int main(){
	BFSQ[qIndex] = head;
	qIndex++;
	BFSonBST();
	int i = 0;
	while (BFSQ[i] != NULL){
		printf("%s",BFSQ[i]);
		i++;
	}
	return 0;
}