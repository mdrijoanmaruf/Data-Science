# C Programming Fundamental Note
## Chapter 1 (variable , conctants) :
### Variable :
```c
int a = 3;      
float b = 3.4;
char c = "c";
```

### Rules for naming variables :
* no commas , blaks allowed.
* First charecter must be an alphabet or underscore (_).
* No special symble allowed withoust (_).

### Constant :
* Integer Constent --> -1, 6, 7, 10
* Real Constant --> -3.22 , 2,5 
* Cahrecter Constant --> 'a' , '$' , '@' (must be enclosed with single inverted commas)

### Comments :
```c
// This is single line comment
/* This is multi line
    comment*/
```

### Library Functons :
```c
%d  // for integers
%f  // for real vlues
%c  // for charecters
```

### Input / Output :
```c
#include <stdio.h>
int main(){
    int a;
    printf("Enter Number :");
    scanf("%d" , &a);       // recived input from user in a
    return 0;
}
```

## Chapter 2 (Instruction and operators) :
### Type of Instraction :
1. Type declareation Instruction
2. Arithmetic Instruction
3. Control Instruction

### Type Declareation Instruction :
```c
int a;
float b;
// Others variation :
int i = 10 ;
int y = i;
int a = 2;
int y = a + y - i;

// Error :
float b = z + 3; // we are trying to use z before defining it.
float z = 10;
// Multi assign :
int a , b, c , d;
a = b = c = d = 30; // values of a, b, c, d will be 30 each.
```
### Arithmetic Instruction :
```c
int i = (3 * 2) + 1;
// * , + , * , / --> operators
// 3, 2, 1 --> operands
// Operands cna be int/float etc.
```

```c
int b = 2, c = 3;
// Legal :
int z; 
z = b * c;

// Illegal :
int z;
b * c = z; 
```

### % operator :
* Modular dicision operator
* Returns the remainder
* Cannot be applied on float
* Sign in same as of numerator (-5 % 2 = -1)

### Operator precedence :
* 1st priority : !
* 2nd priority : * , / , %
* 3rd prioriry : + , -
* 4th prioriry : < , > , <= , >= 
* 5th prioriry : == , !=
* 6th prioriry : &&
* 7th prioriry : ||
* 8th prioriry : =
* Must user bracats.

## Chapter 3 (Conditional Instructions)
* If-else statement
* Switch statement

### If-else statement :
```c
int age = 23;
if(age > 18){
    printf("You can drive.");
}
else if(age > 70){
    printf("You can not drive."); 
}
else{
    printf("You can not drive.");      
}
```

### Relational Operators :
* == , >= ,  <= , > , < , !=
* = is used for assignment
* == is used for equality check

### Logical Operators :
* && , || , !

### One line if else :
```c
// codition ? expression if true : expression if false
(a < 5) ? printf("Under 5") : printf("Not under 5");
```

### Switch case control instruction :
```c
#include <stdio.h>

int main() {
    int monthNumber;

    printf("Enter a number (1-12) representing a month: ");
    scanf("%d", &monthNumber);

    switch (monthNumber) {
        case 1:
            printf("January\n");
            break;
        case 2:
            printf("February\n");
            break;
        case 3:
            printf("March\n");
            break;
        case 4:
            printf("April\n");
            break;
        case 5:
            printf("May\n");
            break;
        case 6:
            printf("June\n");
            break;
        case 7:
            printf("July\n");
            break;
        case 8:
            printf("August\n");
            break;
        case 9:
            printf("September\n");
            break;
        case 10:
            printf("October\n");
            break;
        case 11:
            printf("November\n");
            break;
        case 12:
            printf("December\n");
            break;
        default:
            printf("Invalid month number\n");
            break;
    }

    return 0;
}
```
## Chapter 4 (Loop control Instruction) :
### Type of loops :
* while loop
* do-while loop
* for loop

### While loop :
```c
int count = 1;

while (count <= 5) {
    printf("%d\n", count);
    count++;
}
```

### Increment and decrement operators :
```c
i++ ; // i is increashed by 1 (i = i + 1)
i-- ; // i is decreashed by 1 (i = i - 1)
i+=3 ; // i = i + 3
```

### Do-while loop :
```c
int count = 1;

do {
    printf("%d\n", count);
    count++;
} while (count <= 5);
```

### For loop :
```c
for (int count = 1; count <= 5; count++) {
    printf("%d\n", count);
}
```

### Break :
* Exit from a loop
```c
int count = 1;

while (count <= 10) {
    printf("%d\n", count);
    if (count == 5) {
        break;
    }
    count++;
}
```

### Continue :
* Break 1 loop
```c
for (int count = 1; count <= 10; count++) {
    if (count % 2 != 0) {
        continue;
    }
    printf("%d\n", count);
}
```

## Chapter 5 (Function and Recursion) :
```c
#include <stdio.h>

// Function declaration (prototype)
int add(int a, int b);

int main() {
    // Call the add function and store the result in a variable
    int result = add(5, 3);

    // Print the result
    printf("The sum is: %d\n", result);

    return 0;
}

// Function definition
int add(int a, int b) {
    // Calculate the sum of two numbers
    int sum = a + b;

    // Return the result
    return sum;
}
```
### Types of function calls :
1. Call by value : sending the value agruments.
2. Call by refernce : sending the address of arguments.
```c
#include <stdio.h>

// Function to swap values using call by value
void swapByValue(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

// Function to swap values using call by reference
void swapByReference(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int num1 = 5, num2 = 10;

    printf("Before swapping:\n");
    printf("num1 = %d, num2 = %d\n", num1, num2);

    swapByValue(num1, num2);
    printf("After swapByValue:\n");
    printf("num1 = %d, num2 = %d\n", num1, num2);

    swapByReference(&num1, &num2);
    printf("After swapByReference:\n");
    printf("num1 = %d, num2 = %d\n", num1, num2);

    return 0;
}

```
### Recursion :
```c
#include <stdio.h>

// Recursive function declaration (prototype)
int factorial(int n);

int main() {
    int num;

    // Get input from the user
    printf("Enter a non-negative integer: ");
    scanf("%d", &num);

    // Call the factorial function and print the result
    int result = factorial(num);
    printf("Factorial of %d is %d\n", num, result);

    return 0;
}

// Recursive function definition
int factorial(int n) {
    // Base case: Factorial of 0 is 1
    if (n == 0) {
        return 1;
    }
    // Recursive case: n! = n * (n-1)!
    else {
        return n * factorial(n - 1);
    }
}
```

```c
// how does it work:
// factorial(5)
// 5 x factorial(4)
// 5 x 4 x factorial(3)
// 5 x 4 x 3 x factorial(2)
// 5 x 4 x 3 x 2 x factorial(1)
```

## Chpater 6 (Pointer) :
* A pointer is a variable which sotres the address of another variable.
```c
int i = 100;
int* j = &i;
```
* j is a pointer which store address of i

### The address of operator ( & ) :
* The address of operators is used to obtain the address of a given variable.
* %u is foramt specifier for pointer address.

### The value at address operator ( * ) :
* Used to optain the value present at a given memeory address. It is donoted by '*'

```c
#include <stdio.h>

int main() {
    int num = 42;  // Declare an integer variable
    int *ptr;      // Declare a pointer to an integer

    ptr = &num;    // Assign the address of num to ptr

    printf("Value of num: %d\n", num);
    printf("Address of num: %p\n", &num);
    printf("Value of ptr: %p\n", ptr);  // Pointer holds the address of num
    printf("Value pointed to by ptr: %d\n", *ptr);  // Dereferencing the pointer

    return 0;
}
```

## Chapter 7 (Arrays) :
* One variable capable of storing multiple values.
```c
int marks[10]; // can store int
char name[20]; // can store char

// Index :
marks[0] = 100; // set a value in marks[]
```

### Accessing element :
```c
int marks[10];
scanf("%d" , &marks[0]);        // input 1st value
printf("%d" , marks[0]);        // Output 1st value
```

### Initialising of array :
```c
int cgpa[10] = {1,2,3,4};
float marks[] = {22.2 , 33,4};
```

### Array in memeory :
```c
int arr[3] = {1,2,3};
// This will reserve 4 x 3 = 12 bites in memeory . 4 bites for each integer.
```

### Pointer Arithmatic :
* A pointer can be incremented to point to the next memory location of that type.

### Follwing operation can be performed on a pointes :
1. Adding of a number to a pointer.
2. Subtraction of a number from a pointer.
3. Subtraction of an pointer from another.
4. Comparison of two pointer variable.

### Passing arrays to function :
```c
void pritArr(int* i , int n);  // Funcion prototype.
void pritArr(int i[] , int n); // Another same Funcion prototype.
```

### Multi-dimensional array :
```c
int matrix[2][3] = {{1,2,3}, 
                    {4,5,6}};
matrix[0][0]    // 1
matrix[0][1]    // 2
matrix[1][0]    // 3
```

### 2-D array in memoey :
* A 2-D array like a 1-D arry is stored in memory blocks like this : [[1] [2] [3] [4] [5]....]

## Chapter 8 (String) :
* A string is a 1-D Charecter Array terninated by a null ('\0')

### Initialising string :
```c
char s[] = {'r' ,'i' , 'j' , 'o' , 'a' , 'n' ,'\0'};
```
### Another Shortcut :
```c
char s[] = "rijoan" ; // In this case compailer adds a null character in the last auto.
```

### String in memory :
* Store just like array in memory [['r'] ['i'] ['j'] ['o'] ['a'] ['n'] ['\0']]

### Printing string :
* A string can be printed character by character using printf and %c in loop.

### Another Convenient way :
```c
char s[] = "rijoan";
printf("%s" , s);   // Print the entine string
```

### Strng user input :
```c
char s[];
scanf("%s" , s); // automatic add a null char
```

#### Notes :
* The string should be short enough fit into the array.
* Scanf cannot be used to input multi world string with spaces.

### gets() :
* Used to recive a multi-word string.
```c
char st[30];
gets(st);       // The entered string is stored in st
// Multiple gets() call will be needed for multiple string
```

### puts() :
```c
puts(st);       // prints the string on the next line
```

### Declaring a string using pointer :
```c
char* ptr = "rijoan";
// This tells the compiler to store the string in memory and assigned address is stored in achar pointer.
```

#### Note :
1. Ones a string is defined using char st[] = "rijoan" . It cannot be Re-initialised to something else.
2. A string defined using pointer con be Re-initialised.

### Standard library functions for strings:
#### strlen( ) :
* Used to count the number fo characters in the string excluding the null ('\0')
* Need include <string.h>
```c
char st[] = "rijoan";
int ln = strlen(st);
```

#### strcpy() :
* Used to copy the content of second string into first string passed to it.
```c
char source[] = "rijoan";
char target[100];
strcpy(target , source) // target now contains "rioan"
// target string should have enough capacity to store the source string.
```

#### strcat() :
* Used to concatenate two string.
```c
char s1[] = "rijoan";
char s2[] = "maruf";
strcat(s1, s2)      // now s1 contains "rijoanmaruf"
```

#### strcmp() :
* Used to compare two strings.
* Returns 0 if strings are ecual.
* nagative value if 1st strings mismatching charecters ASCII value is not > 2nd string correnponding mismatching character. It returns positive values otherwise.
```c
strcmp("For" , "joke")      // Positive value
strcmp("Joke" , "For")      // Negative value
```

### Chapter 9 (Structures) :
* Arrays and string can hold similar data but Stuctcture can hold dissimilar data.
* Collection of variable of different dta types under a single name.
* Structure keep the data organized.
* Structure data mamagement easy.
```c
struct employee{
    int code;       // This declares a new user defined data type
    float slary;
    char name[20];
};  // semicolon is important

struct employee e1; // create a struct.
strycpy(e1.name , "rijoan");
e1.code = 100;
e1.salary = 3454.34;
```

### Arrays of structures :
* Just like other arrays we can create an array of structures.
```c
struct employee{
    int code;       // This declares a new user defined data type
    float slary;
    char name[20];
};  // semicolon is important
struct employee fb[100];
fb[0].code = 100;  // we can access data this way
```

### Initialising Structure :
```c
struct employee{
    int code;       
    float slary;
    char name[20];
};
int main(){
    struct employee e1 = {100 , 34.34 , "rijoan"};   // make a new struct with 3 data
    struct employee e2 = {0};       // All element set to 0
}
```

### Structure in memeory :
* Store contigous memory location [[100] [34.34] ["rijoan"]]

### Pointer to structures :

```c
struct employee* ptr ;
ptr = &e1;
prntf("%d" , (*ptr).code); // print structure element using pointer
```

### Arrow operator :
```c
(*pter).code;
ptr->code;      // both are same
```

### Passing structure to a function :
```c
void show(struct employee e1);  // Function prototype
```

### Typedef keyword
```c
typedef struct coumpany{
    int i;
    char name[20];
}cmp;
cmp saif;       // we can use it instand of struct coumpay saif;
```

## Chapter 10 (File Input Output) :
### File Pointer :
* The 'FILE' is a structure which needs to be created for opening the file.
* File pointer is needed for coummunication between the file and the program.

### FILE pointer create :
```c
FILE *ptr;
ptr = fopen("filename.txt" , "r")   // Open filename.txt as reading mode
```

### FILE opening modes :
```c
"r"     // reading              // if the file dose not exist fopen return NULL
"rb"    // reading in binary    // if the file dose not exist fopen return NULL
"w"     // writing              // if the file exist the content will overwrite
"wb"    // writing in binary    // if the file exist the content will overwrite
"a"     // appent               // if the file dose not exist the file will be created
```

### Two types of file :
1. Text file --> .c , .txt
2. Binary file --> .jpg , .dat

### Reading a file :
* A file can be opened for reading as follows
```c
FILE * ptr;     // file pointer variable ptr
ptr = foprn("rijoan.txt" , "r");    // open rijoan.txt as reading mode
int sum;
fscanf(ptr , "%d" , %sum);          //fopen --> file open
// This will read a int from file in sum variable
fclose(ptr);    // closing the file
```

### Writing into a file :
```c
FILE * ptr;
ptr = fopen("rijoan.txt" , "w");        // open rijoan.txt as writing mode
int num = 3443;
fprintf(ptr , "%d" , num);              // writing 3443 into rijoan.txt
fclose(ptr);
```

### fgetc() & fputc() :
* Used to write or read a character from or to a file.
```c
fgetc(ptr);              // read a char from file
fputc('c' ,ptr);         // write a char into a fiel
```

### EOF : End of file :
* fgetc() returns EOF when all the char from a file have been read.
```c
while(1){
    ch = fgetc(ptr);
    if(ch == EOF){
        break;
    }
}
```

## Chapter 11 (Dynamic Memory Allocation) :
* C is a language with some fixed rules of programming . For example : Canging the size of an array is not allowed.

### Dynamic Memory Allocation :
* Dynamic Memory Allocation (DMA) is a way to allocate memory to a data structure during the runtime. we can use DMA functions availabe in c to allocate and free memeory during the runtime.

### Functions for DMA :
```c
malloc();       // memory allocate
calloc();       // memory allocate wilth defalut value o
free();         // free memory
realloc();      // re allocate malloc/calloc
```

### malloc() :
* malloc() stands for memory allocation.
* It takes number of bytes to be allocated as an input and returns a pointer of type void.
```c
ptr = (int*) malloc(30 * sizeof(int));  // 30 --> space for 30 int
    // int* --> casting void pointer to int
    // sizeof(int) --> returns size of 1 int
```
The expression returns a null pointer if the memory cannot be allocated.

### calloc() :
* calloc stands for cantinuous allocation .
* Each memory block with a default value zero.
```c
prt = (float*) calloc(30 , sizeof(float));
    // allocate contigous space in memory for 30 bloks(floats)
```
If the space is not sufficient , memory allocation fails and a NULL pointer is returned.

### free() :
* We can use free() function to de-allocate the memory
* The memory allocated using calloc / malloc is not deallocated automatically.
```c
free(ptr)   // Memory of ptr is released
```

### realloc() :
Sometimes the dynamically allocated memory is insufficient or more then requred.
* reallof() is used to allocate memory of new size using the previous pointer and size.
```c
ptr = realloc(ptr , newsize);
ptr = realloc(ptr , 3 * sizeof(int));
```
Ptr now prints to this new block of memory capable of storing 3 integers.
