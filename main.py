SIMPLE_TAGS = ["canvas", "h1", "h2", "h3", "p", "a", "div", "span", "select"]

def tag(name, *children) -> str:
    html = f'<{name}' 

    for child in children:
        if type(child) == str:
            html += '>' + child
        else:
            html += f' {child}>'

    html += f'</{name}>'

    return html





def div(children: str, props: str) -> str:
    div = '<div>' if props == '' else f'<div {props}>'
    return f'''{div}
            {children}
        </div>'''


def h1(*children):
    return tag('h1', *children)

def div(*children):
    return tag('div', *children)

def main():
    print(div(h1('Hello world')))
    # print(p('hello world'))


if __name__ == "__main__":
    main()
