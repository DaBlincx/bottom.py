"""
decode and encode from and into bottom using the official bottom spec
"""

def encode(text: str) -> str:
    """
    encode a string into bottom
    """
    # get bytes of text and convert each character to decimal
    text_bytes = text.encode()
    text_decimals = [str(byte) for byte in text_bytes]
    output = ""
    for b in [int(b) for b in text_decimals]:
        # b is the decimal representation of the unicode character
        if b == 0:
            output += "❤️"
        while b > 0:
            if b >= 200:
                output += "🫂"
                b -= 200
            elif b >= 50:
                output += "💖"
                b -= 50
            elif b >= 10:
                output += "✨",
                b -= 10
            elif b >= 5:
                output += "🥺",
                b -= 5
            elif b >= 1:
                output += ",",
                b -= 1
            elif b >= 0:
                output += "❤️"
                b -= 0
            else:
                break
        output += "👉👈"
    return output

def decode(text: str) -> str:
    """
    decode a bottom string into the original text
    """
    outputstring = ""
    # split into characters
    characters = text.split("👉👈")
    for character in characters:
        # get the number of each emoji
        num200 = character.count("🫂")
        num50 = character.count("💖")
        num10 = character.count("✨")
        num5 = character.count("🥺")
        num1 = character.count(",")
        num0 = character.count("❤️")
        # get the decimal representation of the character
        decimal = num200 * 200 + num50 * 50 + num10 * 10 + num5 * 5 + num1 * 1 + num0 * 0
        print(
            "num200: " + str(num200), 
            "num50: " + str(num50), 
            "num10: " + str(num10), 
            "num5: " + str(num5), 
            "num1: " + str(num1), 
            "num0", str(num0), 
            "decimal: " + str(decimal), 
            "character: " + chr(decimal)
        )
        # convert to unicode character and add to output
        outputstring += chr(decimal)
        
    return outputstring

def main():
    """
    main function
    """
    import argparse
    parser = argparse.ArgumentParser(description="encode and decode bottom")
    parser.add_argument("-e", "--encode", help="encode text into bottom", action="store_true")
    parser.add_argument("-d", "--decode", help="decode bottom into text", action="store_true")
    parser.add_argument("text", help="text to encode or decode")
    args = parser.parse_args()
    if args.encode:
        print(encode(args.text))
    elif args.decode:
        print(decode(args.text))
    else:
        print("please specify encode or decode")
        ex = encode(args.text)
        print(ex)
        print(decode(ex))

if __name__ == "__main__":
    main()