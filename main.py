def tag(elemen: str, content: str) -> str:
    html = f'<{elemen}>{content}</{elemen}>'
    return html


def div(children: str, props: str) -> str:
    div = '<div>' if props == '' else f'<div {props}>'
    return f'''{div}
            {children}
        </div>'''


def h1(children: str):
    return tag('h1', children)


def main():
    html = div(
               h1('hello world'), 'class="test-class"'
           )
    print(html)


if __name__ == "__main__":
    main()
