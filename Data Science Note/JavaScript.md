# JavaScript

## Chapter 1 (Variable and Data) :

we have some rules writing a JS program . The set of these tules is called syntex in JS.

### Variable :

Variable can be changed during the execution og program

```js
var a = 7; // type int
let b = 7;
```

### Rules of choosing names :

- Latter , digits , undersocres , &, $ sing allowed.
- Must begin with a $ , \_ or a letter
- Js reserved words cannot be used as a variable name.
- rijoan & Rijoan are different variable (case sensitive)

### Var vs Let in Js :

- Var is globally scoped while let & const are block scoped.
- Var can be updated & re-declared within its scope.
- Let can be updated but not re-declared.
- Const can neither be updated not be re-declared.

### Primitive data type :

Primitive data dype are a set of basic datatypes in javascript.
There are 7 premitive datatypes in javascript.

1. Null
2. Number
3. String
4. Symble
5. Boolean
6. Big Int
7. Undefined

### Object :

```js
const item = {
  name: "rijoan maruf",
  salary: "2343",
};
```

## Chapter 2 (Expressions & Conditionals) :

### Oprerators :

#### Arithmetic Operators :

    +   Addition
    -   Subtruaction
    *   Multiplication
    **  Exponentiation (power)
    /   Division
    %   Modulus (Division Remainder)
    ++  Increment
    --  Decrement

#### Assignment Operators :

    =   x = y
    +=  x = x + y
    -=  x = x - y
    *=  x = x * y
    /=  x = x / y
    %=  x = x % y

#### Comparison Operaors :

    ==  Equality check
    === Equal value and equal data type check
    !=  Not equal to
    !== Not equal value and not equal type
    >   Greater than
    <   Less than
    >=  Greater than or equal to
    <=  Less than or equal to
    ?   Ternary Operaotr

#### Logical Operators :

    &&  Logical and
    ||  Logical or
    !   Logical not

### Comments in Js :

```js
// This is single line comment
/* This is multi line 
    comments */
```

### Conditional Statement :

```js
let age = 20;

// Use if, else if, and else statements to determine a message based on the age
if (age < 18) {
  // If the age is less than 18
  console.log("You're a minor.");
} else if (age >= 18 && age < 65) {
  // If the age is 18 or older but less than 65
  console.log("You're an adult.");
} else {
  // If the age is 65 or older
  console.log("You're a senior citizen.");
}
// Output will depend on the value of 'age'
```

### Js ternary operator :

```js
let age = 25;
let message = age < 18 ? "You're a minor." : "You're an adult.";
console.log(message);
```

### User input :

```js
let age = prompt("Enter your age : ");
```

### Switch Statement :

```js
let dayOfWeek = 2;
switch (dayOfWeek) {
  case 1:
    console.log("It's Monday. Time to work.");
    break;
  case 2:
    console.log("It's Tuesday. Still a lot to do.");
    break;
  case 3:
    console.log("It's Wednesday. Halfway through the week.");
    break;
  default:
    console.log("It's not Monday, Tuesday, or Wednesday.");
    break;
}
```

## Loop & Function

### Types of loop :

    for         : loops through a block of code a number of times.
    for in      : loops through the properties of an object
    for of      : loops through the values of an iterable object.
    while       : loops through a block of code while a specified conditions is true.
    do while    : also through a block of code while a specified condition is true.

### For loop :

```js
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

### For in loop :

```js
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
};
// Iterate over the properties of the 'person' object
for (let key in person) {
  console.log(key + ": " + person[key]);
}
```

### For of loop :

```js
const numbers = [1, 2, 3, 4, 5];
// Iterate over the elements of the 'numbers' array using for...of
for (const number of numbers) {
  console.log(number);
}
```

### While loop :

```js
let count = 0;
// Use a while loop to count from 1 to 5
while (count < 5) {
  console.log(count);
  count++;
}
```

### Do-While loop :

```js
let count = 0;
// Use a do...while loop to count from 1 to 5
do {
  console.log(count);
  count++;
} while (count < 5);
```

### Function :

```js
// Define a function that adds two numbers
function addNumbers(a, b) {
  return a + b;
}
// Call the function and store the result
let sum = addNumbers(5, 3);
// Output the result
console.log("Sum:", sum); // Output: Sum: 8
```

```js
// Define an arrow function that adds two numbers
const addNumbers = (a, b) => a + b;
// Call the function and store the result
let sum = addNumbers(5, 3);
// Output the result
console.log("Sum:", sum); // Output: Sum: 8
```

## Chapter 4 (Strings) :

```js
let name = "rijoan"; // create a string.
let name = "rijoan"; // also a string.
```

```js
let backtic_str = `The name "is" Md Rijoan Maruf`; // using backtic
```

```js
let name = "rijoan";
let a = `This is ${name}`;
// will a = This is rijoan
```

### Escape swquence characters :

```js
let name = `Md Rioan\'s Maruf`; // name = Md Rijoan's Maruf
```

    \n  : New line
    \t  : New tab
    \'  : '
    \\  : \
    \b  : Back space

### String properties & Methods :

```js
let name = "rijoan";
name.lenght; // 5
name.toUpperCase(); // RIJOAN
name.toLowerCase(); // rijoan

name.slice(2, 4); // joa  (index start with 0)
name.replace("rijoan", "saif"); // replace rijoan to saif
name.concat(name, "maruf"); // saifmaruf
name.trim(); // remove spaces
name = "saif";
name[0]; // s
```

```js
let text = "This is fox";
let word = "fox";
text.includes(word); // return True if word in text
text.startwith("This"); // return True if text start with "This"
text.endwith("fox"); // return True if text end with "fox"
```

## Chapter 5 (Arrays) :

Arrays are variable which can hold more than one value.

```js
const fruits = ["banana", "apple"];
const a = [234, 45.45, "rijoan", False];
```

### Accessing values :

```js
let arr = [1, 2, 3, 4, 5]; // index start with 0
arr[0]; // 1
arr[2]; // 3
```

### Finding lenght :

```js
arr.lenght; // 5
```

### Changing array value :

```js
let arr = [1, 2, 3, 4, 5];
arr[0] = 100; // now arr = [100,2,3,4,5]
typeof arr; // object
```

### Array methods :

```js
let n = [1, 2, 3, 4];
n.toString(); // n = ['1' , '2' ,'3' , '4']
let x = n.jion("-"); // x = "1-2-3-4"
n.pop(); // Removes the last element from the orignal array.
n.shift(); // Removes the first element from the orignal array.
n.push(100); // add a new value 100 in orignal array
n.unshift(200); // add 200 to the beginning of the array
delete n[0]; // delete 1st index value
```

```js
let x = [1, 2, 3];
let y = [4, 5];
let z = x.concat(y); // now z = [1,2,3,4,5]; returns a new array does not change existing arrray.
```

```js
let str = ["banana", "apple"];
str.shrt(); // sort alphabetically not comparely.
```

```js
let x = [1, 2, 3, 4, 5];
x.slice(0, 2); // wil sice index 0 - 2
```

```js
const x = [1, 2, 3, 4, 5, 6];
x.splice(2, 1, 100, 200); // 2 --> position index , 1 --> Number of element to remove , 100 , 200 wil add .
x.reverse(); // Reverses the elements in the source array.
```

### Looping through arrays :
#### freEach :
```js
const numbers = [1, 2, 3, 4, 5];
numbers.forEach(function (number) {
  console.log(number);
}); // Output : 1, 2, 3,4,5
```
#### map() :
```js
const numbers = [1, 2, 3, 4, 5];

// Use map() to create a new array by doubling each number
const doubled = numbers.map(function(number) {
    return number * 2;
});

console.log(doubled); // Output: [2, 4, 6, 8, 10]
```
#### filter() :
```js
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Use filter() to create a new array containing only even numbers
const evenNumbers = numbers.filter(function(number) {
    return number % 2 === 0;
});

console.log(evenNumbers); // Output: [2, 4, 6, 8, 10]
```

#### reduce() :
```js
const numbers = [1, 2, 3, 4, 5];

// Use reduce() to calculate the sum of all numbers in the array
const sum = numbers.reduce(function(accumulator, currentValue) {
    return accumulator + currentValue;
}, 0); // 0 is the initial value of the accumulator

console.log(sum); // Output: 15
```
#### from() :
```js
const str = "hello";
const charArray = Array.from(str);
console.log(charArray); // Output: ["h", "e", "l", "l", "o"]
```

## Chapter 6 (Js in Browser) :
The borwser has an ambedded engine called the JS engine or Javascript runtime.
### Developer tools :
    Console                 : Log messages, errors, and values for debugging.
    Inspector               : Inspect and modify HTML and CSS of webpages.
    Debugger                : Set breakpoints, step through code, and diagnose issues.
    Network Monitor         : Monitor HTTP requests and responses for performance analysis.
    Sources                 : View and edit JavaScript and CSS files, with debugging features.
    Performance Profiler    : Analyze and optimize application performance.
    Memory Profiler         : Track memory usage and find memory leaks.
    Application Panel       : Manage progressive web app features like service workers and caching.

### The script tag :
Write code in html file using script tag.
```html
<script>
    alert("Hello world")
</script>
<script src = "index.js"></script>
```

### Console object methods :
```js
console.log()                   // Outputs messages or values to the console.
console.info()                  // Logs an informational message.
console.warn()                  // Logs a warning message.
console.error()                 // Logs an error message.
console.clear()                 // Clears the console.
console.table()                 // Displays data as a table.
console.group(), console.groupCollapsed(), console.groupEnd()
                               // Groups console output together (collapsed).
console.assert()                // Logs an error message if assertion is false.
console.count()                 // Counts how many times a line has been executed.
console.time(), console.timeEnd()
                               // Measures time between these functions for profiling.
console.trace()                // Outputs a stack trace to the console.
console.dir()                  // Displays properties of a JavaScript object.
console.dirxml()               // Prints an XML representation of an object.
console.profile(), console.profileEnd()
                               // Starts and stops recording a performance profile.
console.timeStamp()            // Adds a timestamp to the browser's timeline.
console.groupCollapsed(), console.groupEnd()
                               // Groups related output in a collapsed view.
console.count()                // Counts how many times a line has been executed.
```
## Chapter 7 (Working with the DOM) :
Dom tree refers to the HTML page where all the nodes are object. There can be 3 main types of nodes in the Document Object Model (DOM) tree:
* Text nodes
* Element nodes
* Comment nodes
In an HTML page <html> is at the root and <head> and <body> are it's children etc.
A text node is always a leaf of the tree.

### Auto currection :
Some HTML problem is encorrecting by the browser.

### Working with DOM :
```js
document.body       // page body tag
```
document.body can sometimes be null if the JS is written before the body tag.

### Children of an element :
Child nodes --> Element that are direct children . For example head & body are children of <html>

### Child :
```html
<!DOCTYPE html>
<html>
<head>
  <title>DOM Child Nodes Example</title>
</head>
<body>
  <div id="parent">
    <p>First paragraph</p>
    <p>Second paragraph</p>
    <p>Third paragraph</p>
  </div>

  <script>
    // Access the parent element
    const parentElement = document.getElementById("parent");

    // Access the first child node (including non-element nodes)
    const firstChildNode = parentElement.firstChild;

    // Access the first child element
    const firstChildElement = parentElement.firstElementChild;

    // Access the last child node (including non-element nodes)
    const lastChildNode = parentElement.lastChild;

    // Access the last child element
    const lastChildElement = parentElement.lastElementChild;

    // Access all child nodes (including non-element nodes)
    const childNodes = parentElement.childNodes;

    // Output the results to the console
    console.log("First child node:", firstChildNode);
    console.log("First child element:", firstChildElement);
    console.log("Last child node:", lastChildNode);
    console.log("Last child element:", lastChildElement);
    console.log("All child nodes:", childNodes);
  </script>
</body>
</html>
```

#### Note:
Childnodes looks like an array. But it's not actually an array but a collection. We can use Array.from(collection) to convert it into an array.
* They are read only.
* They are live.
* The are iterable using for of loop

### Siblings & the parent :
Siblings are nodes that are children of same parents.

### Element only Navigation :
```js
document.previousElementSibling     --> Previous Sibling
document.nextElementSibling         --> Next Sibling
document.firstElementChild          --> First child
document.lastElementChild           --> Last child
```
### Table links :
```js
table.rows          --> <tr> element
table.caption       --> <caption>
table.tHead         --> <thead>
table.tFoot         --> <tfoot>
table.tBodies       --> <tbody>
```

```js
tbody.rows      //--> Collection of <tr> inside
tr.cells        //--> Collection of the td and th
tr.SectionRowIndex        //--> Index of tr inside tag(element)
td.cellIndex    //--> Number of cell inside enclosind <tr>
tr.rowIndex     //--> Row index number from 0
```

### Searching the DOM :
```js
// getElementById(): Searches for an element by its id attribute.
const elementById = document.getElementById("myElementId");

// querySelector(): Finds the first element that matches a CSS selector.
const elementBySelector = document.querySelector(".myClass");

// querySelectorAll(): Finds all elements that match a CSS selector.
const elementsBySelectorAll = document.querySelectorAll("p");

// getElementsByTagName(): Returns a collection of elements with a specific tag name.
const paragraphs = document.getElementsByTagName("p");

// getElementsByClassName(): Returns a collection of elements with a specific class name.
const elementsByClass = document.getElementsByClassName("myClass");

// Traversing the DOM:
const parentElement = element.parentNode; // Accessing the parent node
const nextSibling = element.nextElementSibling; // Accessing the next sibling element
const previousSibling = element.previousElementSibling; // Accessing the previous sibling element

// Searching within Elements:
const parentElement = document.getElementById("parent"); // Getting the parent element
const childElement = parentElement.querySelector(".child"); // Finding a child element within the parent

// Using Attributes:
const inputElement = document.querySelector('[name="username"]'); // Finding an element by attribute value
```

### Matches , Closest & Contains methods :
```js
// matches(): Checks if an element matches a specific CSS selector.
const elementToCheck = document.getElementById("myElement");
const matchesSelector = elementToCheck.matches(".myClass");

// closest(): Finds the nearest ancestor that matches a specific CSS selector.
const startingElement = document.getElementById("startingElement");
const closestAncestor = startingElement.closest(".ancestorClass");

// contains(): Checks if an element contains another element as its descendant.
const parentElement = document.getElementById("parentElement");
const childElement = document.getElementById("childElement");
const isDescendant = parentElement.contains(childElement);
```

## Chapter 8 (Event & Others DOM properties) :
### Console.dir function :
Console.log shows element DOM tree console.dir show the element as an object with it's properties

### Tag name / Node name :
    tagname     : only exists for element nodes.
    nodename    : defined for only node(text , comment ,etc)

### The innerHtml & OuterHtml :
    1. innerhtml --> Get the HTML inside the element as a string
                 --> Valid for element reads only
    2. outerHtml --> Tag + innerHtml
InnerHtml is valid only for element nodes. For other node types we can use node value or data.

### Text Contant :
Provides access to the text inside the element . Only text and minimus all tags.

### The hidden property :
Specifies whether the element is visible of not.

### Attribute Methods :

```js
// getAttribute(): Retrieves the value of an attribute on an element.
const linkElement = document.getElementById("myLink");
const hrefValue = linkElement.getAttribute("href");

// setAttribute(): Sets the value of an attribute on an element.
linkElement.setAttribute("target", "_blank");

// hasAttribute(): Checks if an element has a specific attribute.
const hasTargetAttribute = linkElement.hasAttribute("target");

// removeAttribute(): Removes a specific attribute from an element.
linkElement.removeAttribute("target");

// classList.add(): Adds one or more classes to an element.
linkElement.classList.add("highlight");

// classList.remove(): Removes one or more classes from an element.
linkElement.classList.remove("highlight");

// classList.toggle(): Toggles a class on or off an element.
linkElement.classList.toggle("active");

// classList.contains(): Checks if an element has a specific class.
const hasHighlightClass = linkElement.classList.contains("highlight");
```

### data-*attribute :
Create custom attribute with "data-" . They are availabel in a property named dataset.

### Insertion methods :
```js
const parentElement = document.getElementById("parent");

// append(): Appends elements or text to the end of an element's content.
const newChild = document.createElement("div");
newChild.textContent = "Appended Text";
parentElement.append(newChild);

// prepend(): Prepends elements or text to the beginning of an element's content.
const newPrependedChild = document.createElement("p");
newPrependedChild.textContent = "Prepended Text";
parentElement.prepend(newPrependedChild);

// before(): Inserts elements or text before an element.
const newBeforeElement = document.createElement("span");
newBeforeElement.textContent = "Inserted Before";
parentElement.before(newBeforeElement);

// after(): Inserts elements or text after an element.
const newAfterElement = document.createElement("span");
newAfterElement.textContent = "Inserted After";
parentElement.after(newAfterElement);

// replaceWith(): Replaces an element with other elements or text.
const replacementElement = document.createElement("div");
replacementElement.textContent = "Replaced Element";
newChild.replaceWith(replacementElement);

// Note: The above methods accept multiple arguments and can insert/replace multiple elements at once.
```

### Insert Adjust HTML /Text / Element :
```js
const parentElement = document.getElementById("parent");

// beforebegin: Inserts content immediately before an element.
const beforeBeginContent = "<p>Before Begin Content</p>";
parentElement.insertAdjacentHTML("beforebegin", beforeBeginContent);

// afterbegin: Inserts content at the beginning of an element's content.
const afterBeginContent = "<p>After Begin Content</p>";
parentElement.insertAdjacentHTML("afterbegin", afterBeginContent);

// beforeend: Inserts content at the end of an element's content.
const beforeEndContent = "<p>Before End Content</p>";
parentElement.insertAdjacentHTML("beforeend", beforeEndContent);

// afterend: Inserts content immediately after an element.
const afterEndContent = "<p>After End Content</p>";
parentElement.insertAdjacentHTML("afterend", afterEndContent);
```

### Node removal :
```js
node.remove();
```
### Classname and classlist :
If we assign something to eleem.classname , it replaces the whole string of classes, often we want to add/remove/toggle a single class.
```js
const element = document.getElementById("myElement");

// Add a class to an element
element.classList.add("newClass");

// Remove a class from an element
element.classList.remove("oldClass");

// Toggle a class on or off an element
element.classList.toggle("active");

// Check if an element has a specific class
const hasNewClass = element.classList.contains("newClass");
```
### Set timeout and set Interval :
```js
let a = setTimeout(function , <delay> , <arg1> , <arg2>);   // delay in ms 
// returns timeid
clearTimeout(a)     // cancel the execution 
```
Set intervel like timeout but its run again and again after time.

### Browser event :
    1. Mouse event : click , contextmenu(right click) , mouseover , mouseout , mousedown , Mouseup , mouse move.
    2. Keybord event : keydown and keyup
    3. From elemtn event : submit , focus etc
    4. Document event : DOM contant looded

### Handling Events :
```html
<input value="hey" onclick="alert('hey')>   // onclick is js function
// or :
elem.onclick = function(){
    // code
}
```
#### Note :
Adding a handler with javascript overwirtes the existing handeler.


### add EventListner & remove EventListener :
```js
element.addEventListener(event , handler);
element.removeEventListener(event , handler);
// handler must be the same function object for to work.
```
### The event object :
```js
elem.onclick = function(event){
    // code
}
```