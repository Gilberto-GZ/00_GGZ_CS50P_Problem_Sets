import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    p1 = re.compile(r"(<iframe(.)+><\/iframe>)")
    p2 = re.compile(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9]*)")

    if re.search(p1, s):
        url = re.search(p2, s)
        if url:
            url_key = url.groups()
            return "https://youtu.be/" + url_key[3]

if __name__ == "__main__":
    main()