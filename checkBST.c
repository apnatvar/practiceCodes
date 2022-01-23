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
int checkBST(BST *head){
	//this function return 0 - if not a BST
	//and 1 if it is a BST
	//One could have also used boolean but i didnt beacuse they are not available by default
	int returnValue;
	if (head==NULL) return 1;
	if (head->leftNode < head)returnValue = checkBST(head->leftNode);
	else return 0;
	if (head->rightNode > head)returnValue = checkBST(head->rightNode);
	else return 0;
	return returnValue;
}
//It is similar to freeing memory alloted to a tree
//except you have to perform certain checks and return appropriate values
int main(){
	if (checkBST(head))printf("It is a BST\n");
	else printf("It is not a BST\n")
	return 0;
}