# ES6笔记

## 2，let var const

var 全局作用域，先使用后声明，undefine
let 局部作用域，或块级作用域。未声明先使用，报错
const声明一个只读的常量。一旦声明，常量的值就不能改变。只在声明所在的块级作用域内有效。
const实际上保证的，并不是变量的值不得改动，而是变量指向的那个内存地址所保存的数据不得改动，const只能保证这个指针是固定的（将一个对象声明为常量必须非常小心）


函数可以在块级作用域声明，考虑到环境导致的行为差异太大，应该避免在块级作用域内声明函数。

ES6 的块级作用域必须有大括号，如果没有大括号，JavaScript 引擎就认为不存在块级作用域。

## 3，变量的解构赋值

解构赋值的规则是，只要等号右边的值不是对象或数组，就先将其转为对象，如果解构不成功，变量的值就等于undefined。

* 数组

```
let [a, b, c] = [1, 2, 3];
let [foo = true] = [];
```

* 对象

```markdown
let { foo, bar } = { foo: 'aaa', bar: 'bbb' };
var {x, y = 5} = {x: 1};
```

嵌套结构

```markdown
const node = {
  loc: {
    start: {
      line: 1,
      column: 5
    }
  }
};

let { loc, loc: { start }, loc: { start: { line }} } = node;
line // 1
loc  // Object {start: Object}
start // Object {line: 1, column: 5}


```
上面代码有三次解构赋值，分别是对loc、start、line三个属性的解构赋值。注意，最后一次对line属性的解构赋值之中，只有line是变量，loc和start都是模式，不是变量。

* 字符串

```markdown
const [a, b, c, d, e] = 'hello';
```

## 4字符串的扩展

* 模板字符串
模板字符串（template string）是增强版的字符串，用反引号（`）标识。它可以当作普通字符串使用，也可以用来定义多行字符串，或者在字符串中嵌入变量。

```markdown
// 普通字符串
`In JavaScript '\n' is a line-feed.`

// 多行字符串
`In JavaScript this is
 not legal.`

console.log(`string text line 1
string text line 2`);

// 字符串中嵌入变量
let name = "Bob", time = "today";
`Hello ${name}, how are you ${time}?`

let greeting = `\`Yo\` World!`;

```

模板字符串甚至还能嵌套。模板字符串的变量之中，又嵌入了另一个模板字符串

* 新增函数

includes()：返回布尔值，表示是否找到了参数字符串。

startsWith()：返回布尔值，表示参数字符串是否在原字符串的头部。

endsWith()：返回布尔值，表示参数字符串是否在原字符串的尾部。

repeat方法返回一个新字符串，表示将原字符串重复n次。

padStart()用于头部补全，padEnd()用于尾部补全

trimStart()消除字符串头部的空格，trimEnd()消除尾部的空格

matchAll()方法返回一个正则表达式在当前字符串的所有匹配


## 正则扩展

字符串对象共有 4 个方法，可以使用正则表达式：match()、replace()、search()和split()。

ES6 将这 4 个方法，在语言内部全部调用RegExp的实例方法

## 数值扩展

* Number.isFinite()用来检查一个数值是否为有限的（finite），即不是Infinity。
如果参数类型不是数值，Number.isFinite一律返回false。

* Number.isNaN()用来检查一个值是否为NaN。

* ES6 将全局方法parseInt()和parseFloat()，移植到Number对象上面，行为完全保持不变。

* Number.isInteger()用来判断一个数值是否为整数。

* Math.trunc方法用于去除一个数的小数部分，返回整数部分。

* Math.sign方法用来判断一个数到底是正数、负数、还是零。对于非数值，会先将其




## 函数

* ES6 允许为函数的参数设置默认值，即直接写在参数定义的后面。参数默认值不是传值的，而是每次都重新计算默认值表达式的值

```markdown
let x = 99;
function foo(p = x + 1) {
  console.log(p);
}

foo() // 100

x = 100;
foo() // 101
```

* 从 ES5 开始，函数内部可以设定为严格模式。

* ES6 引入 rest 参数（形式为...变量名），用于获取函数的多余参数

注意，rest 参数之后不能再有其他参数（即只能是最后一个参数），否则会报错。

```markdown
function add(...values) {
  let sum = 0;

  for (var val of values) {
    sum += val;
  }

  return sum;
}

add(2, 5, 3) // 10

```

* 箭头函数

ES6 允许使用“箭头”（=>）定义函数。

如果箭头函数不需要参数或需要多个参数，就使用一个圆括号代表参数部分。

如果箭头函数的代码块部分多于一条语句，就要使用大括号将它们括起来，并且使用return语句返回。

箭头函数有几个使用注意点。

    （1）函数体内的this对象，就是定义时所在的对象，而不是使用时所在的对象。
    
    （2）不可以当作构造函数，也就是说，不可以使用new命令，否则会抛出一个错误。
    
    （3）不可以使用arguments对象，该对象在函数体内不存在。如果要用，可以用 rest 参数代替。
    
    （4）不可以使用yield命令，因此箭头函数不能用作 Generator 函数。
 
 
 
* 尾调用（Tail Call）
 
 指某个函数的最后一步是调用另一个函数。
 
* 尾递归

函数调用自身，称为递归。如果尾调用自身，就称为尾递归。


* catch 命令参数省略

JavaScript 语言的try...catch结构，以前明确要求catch命令后面必须跟参数，接受try代码块抛出的错误对象。

允许catch语句省略参数

## 数组扩展

扩展运算符（spread）是三个点（...）。它好比 rest 参数的逆运算，将一个数组转为用逗号分隔的参数序列。

```markdown
console.log(...[1, 2, 3])
// 1 2 3

console.log(1, ...[2, 3, 4], 5)
// 1 2 3 4 5

function push(array, ...items) {
  array.push(...items);
}

dict = {
    ...dict,
    'key1':'value1'
}

[...arr1, ...arr2, ...arr3]


// ES5 的合并数组
arr1.concat(arr2, arr3);
// [ 'a', 'b', 'c', 'd', 'e' ]

// ES6 的合并数组
[...arr1, ...arr2, ...arr3]
// [ 'a', 'b', 'c', 'd', 'e' ]
这两种都是浅拷贝

```

* Array.from方法用于将两类对象转为真正的数组：类似数组的对象（array-like object）和可遍历（iterable）的对象（包括 ES6 新增的数据结构 Set 和 Map）。

* Array.of方法用于将一组值，转换为数组。


* 数组实例的find方法，用于找出第一个符合条件的数组成员。

```markdown
[1, 5, 10, 15].find(function(value, index, arr) {
  return value > 9;
}) // 10
```




