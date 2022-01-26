#include <stdio.h>
#include <stdlib.h>

typedef struct BST BST;
struct BST{
	BST* root;
	BST* left;
	BST* right;
	BST* nextInLevel;
};

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
	BFSonBST();
	int i = 0;
	int tempI;
	int combineThese = 0;
	while(i<qIndex){
		tempI = i
		while(--i && BFSQ[combineThese]!=NULL){
			combineThese++;
			BFSQ[combineThese]->nextInLevel = BFSQ[combineThese+1];
		}
		BFSQ[combineThese]->nextInLevel = NULL;
		i = tempI+1;
		i = i*2;
	}
	return 0;
}