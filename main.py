from xml.etree import ElementTree as ET

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

def Button():
    return '<button>test</button>'

def main():
    #print(div(h1('Hello world')))
    # print(p('hello world'))

    print(ET.tostring(ET.Element('div'), encoding="us-ascii", method="html"))
    print(Button())

if __name__ == "__main__":
    main()
