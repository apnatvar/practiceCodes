#include <stdio.h>
#include <stdlib.h>

typedef struct indexed indexed;
struct indexed{
	int startIndex;
	int endIndex;
	indexed* next;
	int count;
};

indexed* head = NULL;
indexed* tail = NULL;


int main(){
	char *str1 ="str1\nstr2\nstr3\nstr4\nstr5\nstr6\nstr7\nstr8\nstr9"
                "\nstr10\nstr11\nstr12\nstr13\nstr14\nstr15\nstr16\nstr17"
                "\nstr18\nstr19\nstr20\nstr21\nstr22\nstr23\nstr24\nstr25"; 
    int i=0;
    int initial = 0;
    int counting = 0;
    while(str1[i]!='\0'){
    	if (str1[i]=='\n'){
    		indexed* temp = (indexed*)malloc(sizeof(indexed));
    		temp->startIndex = initial;
    		temp->endIndex = i;
    		initial=i+1;
    		temp->next = NULL;
    		temp->count = counting;
    		counting++;
    		if (counting == 11){
    			counting--;
    			indexed* deleteThis = head;
    			head = head->next;
    			free(deleteThis);
    		}
    		if (head == NULL){
    			head = temp;
    			tail = temp;
    		}
    		else {
    			tail->next = temp;
    			tail = temp;
    		}
    	}
    	i++;
    }
    if (count==0){
    	printf("Error");
    	exit(0);
    }
    if (counting < 12){
    	indexed* printTemp = head;
    	while (printTemp!=NULL){
    		while (printTemp->startIndex != printTemp->endIndex){
    			printf("%c",str1[printTemp->startIndex]);
    			printTemp->startIndex++;
    		}
    		printTemp = printTemp->next;
    	}
    }
    return 0;
}