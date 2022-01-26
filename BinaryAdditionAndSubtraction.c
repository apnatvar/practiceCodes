#include <stdio.h>
#include <stdlib.h>

int binaryAddition(int a, int b){
	int carry = 0;
	while (a!=0){
		carry = (a & b) <<1;
		b = a^b;
		a = carry;
	}
	return b;
}
int binarySubtraction(int a, int b){
	int carry = 0;
	b = binaryAddition(a,binaryAddition(~b,1));
	return b;
}
int main(){
	printf("Enter Two Number to Add and Subract\n");
	int num1, num2;
	scanf("%d",&num1);
	scanf("%d",&num2);
	int add = binaryAddition(num1, num2);
	int subtract = binarySubtraction(num1, num2);
	printf("%d + %d = %d\n",num1,num2,add);
	printf("%d - %d = %d\n",num1,num2,subtract);
	return 0;
}