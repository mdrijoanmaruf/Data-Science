# CSS Note

## Chapter 1 (First CSS Website) :

### DOM:

DOM stands for Document object model. When a page is loaded the browser crate a DOM of the page which is constructed as a tree of objects.

### HTML id & class Attributes :

- Id is unic identifired for an element
- Class is given element. It is use can more than one element
  We can add multiple classes :

```html
<div id="frist" calss="c1 c2 c3"></div>
```

### Three way to add CSS in HTML :

    1. <style> tag
    2. Inline CSS
    3. External CSS

### CSS Selector :

Select an HTML element for style :

```css
body {
  color: red;
  background: green;
}
```

### Element Selector :

Select element bashed on tag name :

```css
h2 {
  color: blue;
}
```

### ID Selector :

Select Element by ID :

```css
#first {
  color: red;
}
```

### Class Selector :

Select Element by Class :

```css
.red {
  color: white;
}
```

#### Notes:

We can use group selector like this :

```css
h1,
h2,
h3,
div {
  color: blue;
}
```

### Elemnt class :

We can use element calss as a selector like this :

```css
P.red {
  color: red;
  /* all p of class red will get color of red */
}
```

### Universal Selector :

```css
* {
  margin: 0;
  pading: 0;
}
```

If write different code in target one element will consider the last code.

```css
.red {
  color: green;
  color: red;
  /* Color will be red */
}
```

## Chapter 2 (Colors and Background) :

### The color property :

Used to set text color .

```css
p {
  color: red;
}
```

Similarly we can set color for different element.

### Types of color value :

    1. RGB
    2. Hex Code
    3. HSL

### The background color property :

```css
body {
  background-color: red;
}
```

### The background image property :

Used to set an img as the background.

```css
body {
  background-imag: url("rijoan.jpg");
}
```

The image is by default repeted in x ang y directions.

### The background-repeat property :

    repeat-x : repeat horaizontal

    repeat-y : repeat vertical

    no-repeat: no repeat


See more in MDN docs...

### The background size property :

    cover : fits & no empty epace remains

    contain : fits & img is fully visible

    auto : displey in orignal size

    {width} : set width (auto height)

    {width}{height} : set width & height


Always check MDN docs..

### The background position property :

```css
div {
  background-position: left top;
}
```

### The background attachment property :

```css
div {
  background-attachment: fixed;
}
```

### The background shortand :

```css
div {
  background: red url("rijoan.jpg") no-repeat fixed right top;
}
```

## Chapter 3 (CSS Box Model) :

    [[[[Contant] P ] B ] M]     // Pading , Border , Margin

### Setting width & height :

```css
#box {
  height: 70px;
  width: 345px;
}
```

    Total width : width + left/right padding + left/right border + left/right margin

### Setting Margin & Padding :

```css
.box {
  margin: 34px;
  padding: 345px;
}
```

```css
.box {
  margin: 1px 2px 3px 4px;
  /* top : 1 , right 2 , bottom 3 , left 4 */
}
```

```css
.box {
  margin: 7px, 3px;
  /* top & bottom : 7px , left & right : 3px  */
}
```

We can set individual margin & paddin :

```css
.box {
  margin-top: 44px;
  margin-left: 34px;
  margin-right: 24px;
  margin-bottom: 47px;
}
```

Same with padding.

### Setting Borders :

```css
.box {
  border-width: 2px;
  border-style: solid;
  border-color: red;
}
```

### Border Radius :

```css
.div2 {
  border-radius: 6px;
}
```
### Margin Collaps :
Overlaping margin with 2 element.

### Box Sizing :
Padding and border is included in element width & height can be content-box or border-box.
Content-box : Include only contant in width & height.
Border-box : Content + Padding + Border.
```css
div{
    box-sizing : border-box;
}
```

## Chapter 4 (Fonts & Display) :

### display : inline ;
Takes only space requred by  the element. No linebreaks before and after. Setting width / height / margin / padding not allowed.

### display : block ;
Takes full space available in width and break a newline before & after.

### display : inline-block;
Similar to inline but setting height , width , margin , padding is allowed. Element can sit next to each others.

### display : none vs display : hidden 
* With display : none; the element is removed from the document flow It's space is not block.
* With visibility : hidden; the element is hedden but it's space is reserved.

### text-align property :
Used to set boraizontal alignment of a text.
```css
.div1{
    text-align : center;
}
```

### text-decoration property :
Used to decorate text 
Can be overline , line-trough , none , underline

### text-transform property :
Used to specify uppercase and lowercase latters in a text.
```css
p{
    text-transform : uppercase;
}
```

### line-height property :
Used to specify the space between lines.
```css
.div1{
    line-height : 0.7px;
}
```

### Font :
Font playes a important role in the look and feel of a website;

### font-family :
```css
p{
    font-family : "Times new" , "monospace" ;
}
```

### Others font properties :
    1. font-size : size of the font

    2. font-style : font style

    3. font-varient : displayed in small caps.

    4. font-width : width of the font


## Chapter 5 (size , position , lists) :
### Whats wrong with pixels ?
Pixels are relative to viewing devices.

### Reletive lenghts :
    em : relative to the parcent font size.

    rem : relative to the root percent font size.

    vw : relative to 1% view port width

    vh : relative to 1% view port height

    % : related to the percent element

### min/max-height/width property :
CSS has a min height , max-height etc property.

### The position property :
Used to manupulate the location of an element following are the posible values :
```
static : The default positin top / bottom / left / right / z-index has no effect.

relative : Top / bottom / left / right / z-index will work. Will work subject to present elemtnt.

absolute : The element is removed from the flow top / bottom ... etc. Who will work with these main pages.

fixed : This is like absolute but stuck where it will be.

sticky : The element positioned based on user's scroll position.
```

### List style property :
```css
ul{
    list-style : squre inside url("rijan.jpg");
    }
}
```

### Z-index :
The higher its value, the higher it will be.

## Chapter 6 (Flaxbox) :

### The float property :
It just flow the element to words left/right.
```css
float : left;
float : right;
```

### The clear property :
Used to clear the float.

### The CSS flexbox :
Layout align & distribute space among items in a container.
```css
.container{
    display : flex;
    /* Initialige a flexbox */
}
```

### Flex properties for flex container :
```
1. flex-wrap : Can be wrap , no-wrap , worp-reverce.

2. justify-item : Define alignment along main axis.

3. align-item : Define alignment along Y axis.

4. align-contant : Aligns a flex containers lines when there is extra spce in the Y aziz. 
```

### Flex properties for children (Flex item) :
```
1. order : Controls order , default order is 0.

2. align-self : For individual flex item.

3. flex-grow : For a flex item to grow.

4. flex-shrink : For a flex item to shrink.
```

## Chapter 7 (Grid & Media) :
```css
.cont{
    display : grid;
}
```

### grid-column-gap :
Used to adjust the space between the column of a CSS grid.

### grid-row-gap :
Used to adjust the space between the row of a CSS grid.

### grid-gap :
```css
.cont{
    display : grid;
    grid-gap : 23px 100px ;
    /* 23px for row & 100px for column */
}
```

#### Note:
For a single value fo gird-gap both row & column gaps can be set in one value.

### Grid Container Properties :
#### grid-template-column :
Used to specify the width of columns.
```css
.cont{
    display : grid;
    grid-template-column : 66px 33px auto;
}
```

#### grid-template-row :
Used to specify the width of wors.
```css
.cont{
    display : grid;
    grid-template-row : 66px 33px auto;
}
```

#### justify-contant :
Used to alignment whole grid inside the container.

#### align-contant :
Used to vertically align the whole gird inside the container.

### Grid Items Properties :
#### grid-column :
How many columns & items will span.
```css
.grid-item{
    grid-column: 1 / 3;
}
```

#### grid-row :
How many rows an items will span.

We can make an item to short on column 1 and span 3 column like this :
```css
.item{
    grid-column : 1/span 3;
}
```

### CSS Media Queries :
```css
@media only screen and (max-width : 800px){
    body{
        background : red;
    }
}
```