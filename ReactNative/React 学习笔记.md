React 学习笔记

根据[React官方文档](https://react.docschina.org/docs/hello-world.html)学习的相关记录


## JSX 简介

JSX，是一个 JavaScript 的语法扩展

* 在 JSX 语法中，你可以在大括号内放置任何有效的 JavaScript 表达式

```markdown
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>;
```

* 可以在 if 语句和 for 循环的代码块中使用 JSX，将 JSX 赋值给变量，把 JSX 当作参数传入，以及从函数中返回 JSX：

```markdown
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}
```
* 可以通过使用引号，来将属性值指定为字符串字面量

```markdown
const element = <div tabIndex="0"></div>;
const element = <img src={user.avatarUrl}></img>;
```

* JSX 防止注入攻击

React DOM 在渲染所有输入内容之前，默认会进行转义。
它可以确保在你的应用中，永远不会注入那些并非自己明确编写的内容。所有的内容在渲染之前都被转换成了字符串。
这样可以有效地防止 XSS（cross-site-scripting, 跨站脚本）攻击

## 组件

函数组件
```markdown
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

class 组件
```markdown
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

Props 的只读性

组件无论是使用函数声明还是通过 class 声明，都决不能修改自身的 props

这样的函数被称为“纯函数”，因为该函数不会尝试更改入参，且多次调用下相同的入参始终返回相同的结果。

所有 React 组件都必须像纯函数一样保护它们的 props 不被更改


## 声明周期

componentDidMount() 方法会在组件已经被渲染到 DOM 中后运行


## state

使用 setState()修改 State

State 的更新可能是异步的

数据是向下流动的，组件可以选择把它的 state 作为 props 向下传递到它的子组件中























